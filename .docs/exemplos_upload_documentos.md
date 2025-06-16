# Exemplos de Upload de Documentos - API IA Agent

## 📖 Visão Geral

Este documento contém exemplos práticos de como usar a API `/api/v1/documentos/upload` para adicionar contexto ao agente IA. Cada exemplo representa um domínio de negócio diferente e demonstra como a documentação enriquece a geração de testes BDD.

---

## 🛒 E-commerce - Carrinho de Compras

### Request Body
```json
{
  "nome": "regras_carrinho_compras.md",
  "conteudo": "O carrinho de compras permite adicionar até 50 itens por produto. Quando o usuário adiciona um produto já existente, o sistema incrementa a quantidade. O carrinho expira após 30 minutos de inatividade. Produtos com estoque zerado são automaticamente removidos. O frete é calculado baseado no CEP e peso total dos produtos. Cupons de desconto são aplicados sobre o subtotal, excluindo o frete. O sistema valida se o usuário está logado antes de finalizar a compra.",
  "projeto": "ecommerce"
}
```

### Comando cURL
```bash
curl -X POST "http://localhost:8000/api/v1/documentos/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "regras_carrinho_compras.md",
    "conteudo": "O carrinho de compras permite adicionar até 50 itens por produto. Quando o usuário adiciona um produto já existente, o sistema incrementa a quantidade. O carrinho expira após 30 minutos de inatividade. Produtos com estoque zerado são automaticamente removidos. O frete é calculado baseado no CEP e peso total dos produtos. Cupons de desconto são aplicados sobre o subtotal, excluindo o frete. O sistema valida se o usuário está logado antes de finalizar a compra.",
    "projeto": "ecommerce"
  }'
```

### História de Usuário Relacionada
```json
{
  "titulo": "Adicionar produto ao carrinho",
  "descricao": "Como cliente, desejo adicionar produtos ao carrinho para posterior compra"
}
```

---

## 🏦 Sistema Bancário - Transferências PIX

### Request Body
```json
{
  "nome": "especificacao_transferencia_pix.md",
  "conteudo": "Transferências PIX são processadas instantaneamente em horário comercial (6h às 22h). Fora desse horário, são agendadas para o próximo dia útil. O limite diário para pessoas físicas é R$ 20.000. Chaves PIX válidas incluem CPF, email, telefone e chave aleatória. O sistema valida a chave PIX antes de processar a transferência. Em caso de chave inválida, retorna erro específico. Transferências acima de R$ 5.000 requerem confirmação por SMS. O extrato é atualizado imediatamente após a transferência.",
  "projeto": "sistema-bancario"
}
```

### Comando cURL
```bash
curl -X POST "http://localhost:8000/api/v1/documentos/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "especificacao_transferencia_pix.md",
    "conteudo": "Transferências PIX são processadas instantaneamente em horário comercial (6h às 22h). Fora desse horário, são agendadas para o próximo dia útil. O limite diário para pessoas físicas é R$ 20.000. Chaves PIX válidas incluem CPF, email, telefone e chave aleatória. O sistema valida a chave PIX antes de processar a transferência. Em caso de chave inválida, retorna erro específico. Transferências acima de R$ 5.000 requerem confirmação por SMS. O extrato é atualizado imediatamente após a transferência.",
    "projeto": "sistema-bancario"
  }'
```

### História de Usuário Relacionada
```json
{
  "titulo": "Transferir dinheiro via PIX",
  "descricao": "Como correntista, desejo transferir dinheiro via PIX para outros bancos"
}
```

---

## 👥 Sistema de RH - Gestão de Férias

### Request Body
```json
{
  "nome": "politica_ferias_funcionarios.md",
  "conteudo": "Funcionários adquirem direito a 30 dias de férias após 12 meses de trabalho. Férias podem ser divididas em até 3 períodos, sendo um mínimo de 14 dias corridos. O funcionário deve solicitar férias com 30 dias de antecedência. Férias coincidentes na mesma equipe não são permitidas sem aprovação gerencial. O sistema calcula automaticamente o adicional de 1/3 constitucional. Funcionários com mais de 50 anos têm prioridade na escolha do período. Férias não gozadas vencem em 23 meses após aquisição.",
  "projeto": "rh-system"
}
```

### Comando cURL
```bash
curl -X POST "http://localhost:8000/api/v1/documentos/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "politica_ferias_funcionarios.md",
    "conteudo": "Funcionários adquirem direito a 30 dias de férias após 12 meses de trabalho. Férias podem ser divididas em até 3 períodos, sendo um mínimo de 14 dias corridos. O funcionário deve solicitar férias com 30 dias de antecedência. Férias coincidentes na mesma equipe não são permitidas sem aprovação gerencial. O sistema calcula automaticamente o adicional de 1/3 constitucional. Funcionários com mais de 50 anos têm prioridade na escolha do período. Férias não gozadas vencem em 23 meses após aquisição.",
    "projeto": "rh-system"
  }'
```

### História de Usuário Relacionada
```json
{
  "titulo": "Solicitar férias",
  "descricao": "Como funcionário, desejo solicitar minhas férias anuais escolhendo o período"
}
```

---

## 🎓 Sistema Educacional - Matrícula

### Request Body
```json
{
  "nome": "processo_matricula_alunos.md",
  "conteudo": "O processo de matrícula ocorre em 3 fases: pré-matrícula online, entrega de documentos e confirmação de pagamento. Alunos veteranos têm prioridade na escolha de disciplinas. Cada disciplina tem pré-requisitos obrigatórios que devem ser atendidos. O sistema bloqueia matrícula em disciplinas com horário conflitante. Limite máximo de 8 disciplinas por semestre. Disciplinas com menos de 10 alunos são canceladas. Trancamento de matrícula pode ser feito até 30 dias após início das aulas com devolução de 70% da mensalidade.",
  "projeto": "sistema-educacional"
}
```

### Comando cURL
```bash
curl -X POST "http://localhost:8000/api/v1/documentos/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "processo_matricula_alunos.md",
    "conteudo": "O processo de matrícula ocorre em 3 fases: pré-matrícula online, entrega de documentos e confirmação de pagamento. Alunos veteranos têm prioridade na escolha de disciplinas. Cada disciplina tem pré-requisitos obrigatórios que devem ser atendidos. O sistema bloqueia matrícula em disciplinas com horário conflitante. Limite máximo de 8 disciplinas por semestre. Disciplinas com menos de 10 alunos são canceladas. Trancamento de matrícula pode ser feito até 30 dias após início das aulas com devolução de 70% da mensalidade.",
    "projeto": "sistema-educacional"
  }'
```

### História de Usuário Relacionada
```json
{
  "titulo": "Realizar matrícula em disciplinas",
  "descricao": "Como aluno, desejo me matricular nas disciplinas do próximo semestre"
}
```

---

## 📱 Sistema de Delivery - Pedidos

### Request Body
```json
{
  "nome": "regras_pedidos_delivery.md",
  "conteudo": "Pedidos podem ser feitos apenas em restaurantes com status 'Aberto'. O tempo de entrega é calculado baseado na distância e movimento dos entregadores. Taxa de entrega varia de R$ 2,99 a R$ 12,99 conforme a distância. Pedidos acima de R$ 35,00 têm frete grátis. O sistema permite cancelamento até 5 minutos após confirmação. Formas de pagamento aceitas: cartão, PIX e dinheiro. Avaliação do pedido é obrigatória após entrega. Cupons promocionais não são cumulativos.",
  "projeto": "delivery-app"
}
```

### Comando cURL
```bash
curl -X POST "http://localhost:8000/api/v1/documentos/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "regras_pedidos_delivery.md",
    "conteudo": "Pedidos podem ser feitos apenas em restaurantes com status '"'"'Aberto'"'"'. O tempo de entrega é calculado baseado na distância e movimento dos entregadores. Taxa de entrega varia de R$ 2,99 a R$ 12,99 conforme a distância. Pedidos acima de R$ 35,00 têm frete grátis. O sistema permite cancelamento até 5 minutos após confirmação. Formas de pagamento aceitas: cartão, PIX e dinheiro. Avaliação do pedido é obrigatória após entrega. Cupons promocionais não são cumulativos.",
    "projeto": "delivery-app"
  }'
```

### História de Usuário Relacionada
```json
{
  "titulo": "Fazer pedido de comida",
  "descricao": "Como cliente, desejo fazer um pedido de comida para entrega em casa"
}
```

---

## ✅ Response Padrão

Todos os uploads retornam uma resposta similar a esta:

```json
{
  "nome": "regras_carrinho_compras.md",
  "projeto": "ecommerce",
  "status": "Documento inserido com sucesso",
  "total_caracteres": 456
}
```

---

## 🔍 Como Verificar o Contexto

Após fazer upload dos documentos, você pode verificar se estão sendo encontrados:

```bash
curl "http://localhost:8000/api/v1/documentos/buscar/carrinho?limit=3"
```

Response esperado:
```json
{
  "query": "carrinho",
  "total_encontrados": 1,
  "documentos": [
    "O carrinho de compras permite adicionar até 50 itens por produto..."
  ]
}
```

---

## 🎯 Benefícios do RAG

Com esses documentos carregados, quando você gerar testes para histórias relacionadas, a IA usará automaticamente o contexto relevante para criar cenários mais precisos e realistas, incluindo:

- Regras de negócio específicas
- Limitações do sistema
- Fluxos de aprovação
- Validações obrigatórias
- Comportamentos esperados

**Resultado**: Testes BDD mais aderentes à realidade do sistema! 