# Plano de Estudo e Portfólio no GitHub

Este guia apresenta uma rotina diária de estudo, bem como estratégias para usar o GitHub como vitrine do seu conhecimento. Adapte conforme o seu ritmo e objetivos profissionais.

## Objetivos Gerais
- Reforçar fundamentos de programação e desenvolvimento.
- Construir um portfólio que mostre evolução e domínio técnico.
- Manter consistência com commits, documentação e testes.

## Organização do Portfólio
1. **Reposição de habilidades**: crie repositórios temáticos (ex.: `fundamentos`, `projetos-web`, `data-science`).
2. **Documentação clara**: cada projeto deve ter `README` com descrição, tecnologias, instruções de uso e próximos passos.
3. **Commits descritivos**: use mensagens que expliquem o "porquê" da mudança.
4. **Issues e projetos**: registre ideias em issues e use o GitHub Projects para planejar tarefas.
5. **Apresentação profissional**: configure o README do perfil destacando stack, projetos e metas.

## Rotina Diária (aprox. 2h30 a 3h)
> Ajuste o tempo conforme disponibilidade. Se não puder cumprir tudo, priorize a sessão principal do dia.

| Bloco | Duração | Atividade | Objetivo |
|-------|---------|-----------|----------|
| Aquecimento | 15 min | Ler artigos curtos, changelog ou documentação. | Atualizar-se e treinar leitura técnica. |
| Revisão | 30 min | Resolver exercícios ou refazer katas relacionados a conceitos anteriores. | Fixar fundamentos e identificar lacunas. |
| Sessão principal | 1h30 | Desenvolver uma funcionalidade ou projeto pequeno no GitHub. | Evoluir portfólio e praticar versionamento. |
| Fechamento | 15-30 min | Escrever notas no `README`, abrir issues, fazer code review pessoal. | Consolidar aprendizado e mostrar profissionalismo. |

## Rotina Semanal
- **Segunda**: Definir metas e abrir issues no projeto em andamento.
- **Terça a quinta**: Implementar funcionalidades incrementais; priorize testes e documentação.
- **Sexta**: Revisar código, preparar release ou demo, escrever retrospectiva no repositório (arquivo `LOG.md`).
- **Sábado**: Contribuir em projeto open source ou revisar PRs antigos.
- **Domingo**: Descanso ativo (assistir talks, planejar semana).

## Projetos Sugeridos (ciclos mensais)
1. **Mês 1 — Fundamentos**: soluções de algoritmos, APIs simples, aplicações CLI.
2. **Mês 2 — Web/App**: frontend responsivo, integração com API, testes automatizados.
3. **Mês 3 — Especialização**: escolha uma área (dados, mobile, DevOps) e entregue um MVP completo.

Repita o ciclo com dificuldade crescente e registre aprendizados em um blog ou README de progresso.

## Boas Práticas Adicionais
- Configure GitHub Actions para validar builds e testes.
- Escreva posts curtos (no README do perfil ou blog) contando desafios e soluções.
- Compartilhe projetos no LinkedIn, destacando tecnologias e problemas resolvidos.
- Participe de comunidades (Discord, Slack, fóruns) para trocar feedback.
- Faça code reviews do próprio trabalho anotando melhorias futuras.

## Indicadores de Evolução
- Número de commits consistentes ao longo da semana.
- Issues concluídas versus planejadas.
- Projetos completos com documentação e testes.
- Feedback recebido (estrelas, forks, comentários) e incorporado.

## Ferramenta de apoio: verificação passiva de Log4j

O repositório inclui o script `passive_log4j_check.py`, que realiza uma checagem passiva em endpoints HTTP/HTTPS em busca de indícios da vulnerabilidade Log4Shell (Log4j). O script **não** executa exploração ativa: ele apenas busca evidências em respostas e cabeçalhos.

### Requisitos
- Python 3.8+
- Dependências listadas em `requirements.txt`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

### Uso

```bash
python passive_log4j_check.py https://example.com outro-alvo.com
```

Para cada URL fornecida o script:
- Normaliza o esquema (https por padrão).
- Faz uma requisição GET com timeout de 10 segundos.
- Analisa cabeçalhos, corpo e links para identificar padrões relacionados a Log4j/Log4Shell.
- Exibe um resumo com possíveis indícios encontrados.

Use somente em ambientes onde você tem autorização explícita.

Mantenha disciplina, ajuste o plano conforme necessário e celebre cada conquista. O importante é demonstrar crescimento contínuo e profissionalismo em público.
