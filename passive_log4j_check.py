#!/usr/bin/env python3
"""
passive_log4j_check.py
Checagem passiva por indícios de Log4j/Log4Shell (não-invasivo — NÃO explora).
Uso: python passive_log4j_check.py https://example.com another-target.com
"""
import sys
import re
import requests
from urllib.parse import urlparse

# timeouts e user-agent básico
TIMEOUT = 10
HEADERS = {
    "User-Agent": "PassiveLog4jChecker/1.0 (+https://example.com/)",
    "Accept": "*/*"
}

# padrões a buscar (sensíveis, mas passivos)
PATTERNS = {
    "log4j_string": re.compile(r"log4j", re.IGNORECASE),
    "log4j_jar": re.compile(r"log4j[-_.]core[-_.]2\.\d+", re.IGNORECASE),
    "jndi_pattern": re.compile(r"\$\{.*jndi:.*\}", re.IGNORECASE),
    "java_stack": re.compile(r"(?:(Exception in thread|at [\w\.]+\(|java\.)|Caused by:)", re.IGNORECASE),
    "server_java": re.compile(r"(tomcat|jetty|jboss|glassfish|wildfly|payara|jetty)", re.IGNORECASE)
}

def fetch(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True, verify=True)
        return r
    except requests.exceptions.SSLError:
        # tentar sem verificação ssl (opcional, cuidado)
        try:
            r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True, verify=False)
            return r
        except Exception:
            return None
    except Exception:
        return None

def analyze_response(r):
    results = []
    if r is None:
        return ["no_response"]

    # cabeçalhos
    server = r.headers.get("Server", "") or r.headers.get("X-Powered-By", "")
    if server and PATTERNS["server_java"].search(server):
        results.append(f"server_header_indicates_java: {server}")

    # procurar strings no corpo
    body = r.text or ""
    for name, pattern in PATTERNS.items():
        if pattern.search(body):
            results.append(f"matched_{name}")

    # procurar em URLs (links) expostos no HTML por nomes de jar
    hrefs = re.findall(r'href=["\']?([^"\'>\s]+)', body, re.IGNORECASE)
    for href in set(hrefs):
        if PATTERNS["log4j_jar"].search(href):
            results.append(f"exposed_jar_link:{href}")

    # status code info
    results.append(f"status:{r.status_code}")
    return results

def normalize_target(t):
    p = urlparse(t if '://' in t else 'https://' + t)
    if not p.scheme:
        return 'https://' + t
    return p.geturl()

def main(targets):
    for t in targets:
        url = normalize_target(t)
        print(f"\n--- {url} ---")
        r = fetch(url)
        if not r:
            print("Sem resposta / falha ao conectar.")
            continue
        findings = analyze_response(r)
        for f in findings:
            print(" -", f)
        # dica rápida
        if any(x.startswith("matched_jndi_pattern") for x in findings) or any("log4j_string" in x for x in findings):
            print(">>> Possível indicação encontrada (passiva). Recomenda-se investigação mais profunda com autorização.")
        else:
            print("Nenhum indício passivo detectado nesta requisição.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python passive_log4j_check.py <url1> [url2] ...")
        sys.exit(1)
    main(sys.argv[1:])
