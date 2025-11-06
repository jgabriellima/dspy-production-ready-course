# Landing Pages DSPy

Este diretório contém duas landing pages profissionais:

1. **Curso** (`index.html`) - Landing page para curso online
2. **Livro** (`prevenda.html`) - Página de pré-venda do livro técnico

## 📁 Estrutura

```
web/
├── index.html           # Landing page do CURSO
├── prevenda.html        # Landing page do LIVRO (pré-venda) ⭐ NOVO
├── copy.md             # Conteúdo e textos (curso)
├── DESIGN_SYSTEM.md    # Sistema de design e guidelines
├── serve.sh            # Script para servir localmente
└── README.md           # Este arquivo
```

## 🎯 Diferenças Entre as Páginas

### index.html (Curso)
- **Produto**: Curso online DSPy
- **Foco**: Módulos, aprendizado prático
- **Preço**: R$ 579/ano (renovação automática)
- **CTA**: "Matricular Agora"
- **Estrutura**: 8 módulos progressivos
- **Público**: Quem quer aprender com aulas

### prevenda.html (Livro) ⭐
- **Produto**: Livro técnico físico/digital
- **Foco**: Conteúdo completo, referência técnica production-ready
- **Preço**: **R$ 197** (pré-venda) / R$ 297 (regular)
- **CTA**: "Reservar com Desconto"
- **Estrutura**: 17 capítulos + 7 apêndices (600-900 páginas)
- **Público**: Engenheiros ML, desenvolvedores AI, pesquisadores
- **Bônus**: Acesso antecipado, atualizações por 1 ano, nome nos agradecimentos

## 🚀 Como Usar

### Servir Localmente

```bash
cd web/
chmod +x serve.sh
./serve.sh
```

**Acessar:**
- Curso: `http://localhost:8000/index.html`
- Livro (Pré-venda): `http://localhost:8000/prevenda.html` ⭐

Ou usando Python diretamente:

```bash
cd web/
python3 -m http.server 8000
```

### Usando outros servidores

**Node.js (npx):**
```bash
cd web/
npx serve
```

**PHP:**
```bash
cd web/
php -S localhost:8000
```

## 🎨 Tecnologias

- **Tailwind CSS**: Framework CSS utility-first (via CDN)
- **GSAP**: Biblioteca de animações + ScrollTrigger
- **Google Fonts**: Inter + JetBrains Mono
- **Vanilla JS**: Sem frameworks pesados

## 🎨 Design System

Ver: [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)

**Paleta de Cores:**
- Primary: #6366f1 (Indigo)
- Secondary: #8b5cf6 (Purple)
- Accent: #ec4899 (Pink)
- Success: #10b981 (Green)
- Warning: #f59e0b (Orange)
- Error: #ef4444 (Red)

**Dark Theme:**
- Background Primary: #0a0e1a
- Background Secondary: #0f172a
- Background Tertiary: #1e293b

## ✨ Features Implementadas

### Página de Pré-Venda (prevenda.html) ⭐

#### 🎯 Hero Section
- Badge de oferta com animação pulse
- Título gradient impactante
- Dois CTAs (primário + secundário)
- Social proof (17 capítulos, código production-ready, 600+ páginas)
- Preview 3D do livro com efeito hover

#### 📊 Problem/Solution
- Identificação clara de 3 problemas principais
- Solução com 4 métricas visuais
- Cards com hover effect suave

#### 📚 Conteúdo Detalhado
- **Parte 1**: Fundamentos (3 capítulos)
- **Parte 2**: Arquiteturas Cognitivas (4 capítulos)
  - Sequential/Pipeline
  - Hierarchical
  - Collaborative/Debate
  - Reflexive/Self-Critique
- **Parte 3**: Otimização & Fine-Tuning (6 capítulos)
- **Parte 4**: Enterprise & Production (4 capítulos)
- Preview de todos os 17 capítulos com descrições
- Tags por categoria
- Bônus: 7 apêndices + GitHub repo

#### 👤 Seção de Autor
- Bio profissional
- Credibilidade técnica
- Design clean

#### 💰 Pricing Comparativo
- **Pré-venda**: R$ 197 (destaque visual)
- **Regular**: R$ 297 (após lançamento)
- Comparação lado a lado
- Lista de benefícios detalhada
- Badge "Melhor Oferta" animado
- Garantia 30 dias + parcelamento 12x
- 3 bônus exclusivos para pré-venda

#### 🎯 CTA Final + FAQ
- Call to action forte
- 5 perguntas frequentes
- Garantias e segurança
- Informações de lançamento

#### 🎨 UX Features
- **Progress bar** de scroll no topo
- Animações GSAP suaves em scroll
- Smooth scroll para âncoras
- Responsivo completo (mobile-first)
- Cards com hover states elegantes
- Floating animation no book preview

### Página do Curso (index.html)

#### Features
- ASCII art animado no hero
- 8 módulos detalhados
- Terminal code snippets
- Pricing único (R$ 579/ano)
- Learning path visualization
- Módulos progressivos com código

## 📝 Customização

### Modificar Preços

**Pré-venda (prevenda.html):**
```html
<!-- Seção #preco, linha ~700 -->
<div class="text-5xl font-bold gradient-text mb-2">
    R$ 197<span class="text-2xl">,00</span>
</div>
```

**Curso (index.html):**
```html
<!-- Seção #pricing, linha ~440 -->
<div class="text-6xl md:text-7xl font-bold gradient-text mb-2">
    R$ 579<span class="text-3xl">,00</span>
</div>
```

### Modificar Timeline de Lançamento

```html
<!-- Em prevenda.html, linha ~850 -->
<div class="text-xs text-tertiary">
    Lançamento previsto: Q1 2025
</div>
```

### Adicionar Badge de Urgência

```html
<span class="badge badge-accent">
    ⏰ Últimas 10 vagas • 72h restantes
</span>
```

### Email de Contato (CTAs)

**Pré-venda:**
```html
<!-- Linha ~920 -->
<a href="mailto:joao@example.com?subject=Reserva%20Livro%20Multi-Agent%20DSPy">
```

**Curso:**
```html
<!-- Linha ~540 -->
<a href="mailto:contato@dspcourse.com">
```

### Modificar Cores

As cores estão centralizadas em variáveis CSS no `:root`:

```css
:root {
    --color-primary: #6366f1;
    --color-secondary: #8b5cf6;
    --color-accent: #ec4899;
    --color-success: #10b981;
    /* etc */
}
```

### Adicionar Animações GSAP

```javascript
gsap.from("#meuElemento", {
    scrollTrigger: {
        trigger: "#meuElemento",
        start: "top 80%",
        toggleActions: "play none none none"
    },
    duration: 0.8,
    y: 50,
    opacity: 0,
    ease: "power3.out"
});
```

## 🚀 Deploy

### Netlify

1. Conecte o repositório GitHub
2. Configure:
   - Build command: (vazio)
   - Publish directory: `web/`
3. Deploy!

**Custom domains:**
- Curso: `curso.seudominio.com` → `/index.html`
- Livro: `livro.seudominio.com` ou `book.seudominio.com` → `/prevenda.html`

### Vercel

```bash
cd web/
vercel --prod
```

Configure o diretório como `web/`.

### GitHub Pages

1. Vá em Settings → Pages
2. Source: Deploy from branch
3. Branch: `main`, folder: `/web`
4. Save

**Acessar:**
- `https://seu-usuario.github.io/repo/index.html`
- `https://seu-usuario.github.io/repo/prevenda.html`

## ⚡ Performance

### Atual (Dev)
- Tailwind via CDN (~3MB, mas cacheado)
- GSAP via CDN
- Google Fonts

### Recomendações para Produção

#### Build Tailwind Customizado
Reduz de 3MB → 10KB!

```bash
# Instalar Tailwind
npm install -D tailwindcss

# Criar config
npx tailwindcss init

# tailwind.config.js
module.exports = {
  content: ["./prevenda.html", "./index.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}

# Build
npx tailwindcss -o output.css --minify
```

#### Outras Otimizações
- [ ] Minificar HTML (gzip)
- [ ] Self-host fontes (reduz latência)
- [ ] Preload assets críticos
- [ ] Lazy loading em imagens (quando adicionar)
- [ ] Service Worker (PWA)

**Lighthouse Target:**
- Performance: 90+
- Accessibility: 95+
- Best Practices: 100
- SEO: 100

## ♿ Acessibilidade

### ✅ Implementado
- Contraste WCAG AA/AAA
- Navegação por teclado
- Semantic HTML (section, nav, footer)
- Focus states visíveis
- Headings hierárquicos

### 🔄 TODO
- [ ] ARIA labels em ícones decorativos
- [ ] Alt text em imagens (quando adicionar)
- [ ] Skip to content link
- [ ] Screen reader testing com VoiceOver/NVDA

## 📱 Responsividade

Mobile-first design testado em:

**Breakpoints:**
- **sm**: 640px (mobile landscape)
- **md**: 768px (tablet)
- **lg**: 1024px (desktop)
- **xl**: 1280px (large desktop)

**Adaptações:**
- Grid: 1 col → 2 cols → 3 cols
- Fontes: `clamp()` para escalar automaticamente
- Navegação: Links escondem em mobile (considerar hamburger menu)
- Imagens: 100% width em mobile

**Testar em:**
- [ ] iPhone 13/14 (Safari)
- [ ] Android (Chrome)
- [ ] iPad (Safari)
- [ ] Desktop (Chrome/Firefox/Safari)

## 🔍 SEO

### Meta Tags (prevenda.html)

```html
<title>Pré-Venda: Sistemas Multi-Agente para Produção com DSPy | Livro Técnico</title>
<meta name="description" content="Reserve sua cópia do livro técnico mais completo sobre Multi-Agent Systems com DSPy...">
<meta name="keywords" content="DSPy, Multi-Agent, AI Agents, LLM, Machine Learning, Python, Book">
<meta name="author" content="João Gabriel Lima">
```

### Open Graph

```html
<meta property="og:title" content="Pré-Venda: Sistemas Multi-Agente para Produção com DSPy">
<meta property="og:description" content="O guia técnico definitivo para construir agentes multi-agent production-ready">
<meta property="og:type" content="website">
```

### TODO SEO
- [ ] `og:image` (imagem de preview 1200x630)
- [ ] Twitter Card
- [ ] Canonical URL
- [ ] Structured Data (Book schema)
- [ ] Sitemap.xml
- [ ] robots.txt

### Structured Data Example (Book)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": "Sistemas Multi-Agente para Produção com DSPy",
  "author": {
    "@type": "Person",
    "name": "João Gabriel Lima"
  },
  "offers": {
    "@type": "Offer",
    "price": "197.00",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/PreOrder"
  }
}
</script>
```

## 📊 Analytics

### Google Analytics 4

```html
<!-- Antes de </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Eventos para Trackear

**Pré-venda:**
- `click_cta_hero` - Clique no CTA principal
- `view_pricing` - Scroll até seção de preços
- `click_reserve` - Clique em "Reservar Agora"
- `expand_faq` - Clique em FAQ
- `time_on_page` - Tempo médio

**Curso:**
- `click_enroll` - Clique em "Matricular"
- `view_modules` - Scroll até módulos
- `click_pricing` - Scroll até preço

### Custom Events (GTM)

```javascript
// Exemplo: trackear clique em CTA
document.querySelector('.cta-button').addEventListener('click', () => {
    gtag('event', 'click_reserve', {
        'event_category': 'engagement',
        'event_label': 'hero_cta'
    });
});
```

## 🧪 A/B Testing

### Elementos para Testar (Pré-venda)

1. **Títulos**
   - A: "Multi-Agent Systems para Produção"
   - B: "Domine Agentes Multi-Agent em Produção"

2. **Preços**
   - A: R$ 197
   - B: R$ 247
   - C: R$ 177

3. **CTAs**
   - A: "Reservar Agora por R$ 197"
   - B: "Garantir Desconto de Lançamento"
   - C: "Comprar com 33% OFF"

4. **Cores de CTA**
   - A: Gradient Indigo→Purple
   - B: Solid Green
   - C: Solid Pink

5. **Social Proof**
   - A: Números (17 capítulos, 600+ páginas)
   - B: Depoimentos
   - C: Logotipos de empresas

### Tools Sugeridas
- Google Optimize
- Optimizely
- VWO
- Unbounce

## 🛠️ Manutenção

### Checklist Pré-Lançamento

#### prevenda.html
- [ ] Testar todos os links (âncoras e externos)
- [ ] Verificar email de contato nos CTAs
- [ ] Confirmar preços e descontos
- [ ] Revisar copy (typos, gramática)
- [ ] Testar responsividade (4+ devices)
- [ ] Validar HTML (W3C Validator)
- [ ] Lighthouse score (90+)
- [ ] Testar animações GSAP
- [ ] Social sharing preview (Facebook, Twitter, LinkedIn)
- [ ] Testar formulário de contato (se houver)

#### index.html
- [ ] Mesmas verificações acima
- [ ] Testar todos os 8 módulos

### Atualizações Regulares

**Semanais:**
- [ ] Atualizar countdown (se houver)
- [ ] Monitorar analytics
- [ ] Responder emails de interesse

**Mensais:**
- [ ] Revisar copy
- [ ] Ajustar preços conforme timeline
- [ ] Adicionar social proof (pré-vendas realizadas)
- [ ] Atualizar FAQ com perguntas comuns

**Pré-Lançamento:**
- [ ] Mudar CTAs de "Reservar" para "Comprar"
- [ ] Atualizar preço para regular
- [ ] Remover badges de urgência
- [ ] Adicionar seção de reviews

## 🐛 Suporte e Troubleshooting

### Problemas Comuns

#### 1. Animações não funcionam
**Sintoma:** Cards não animam ao scroll

**Solução:**
```javascript
// Abra console e verifique:
console.log(typeof gsap); // deve retornar "object"
console.log(typeof ScrollTrigger); // deve retornar "object"
```

Se retornar `undefined`, verifique se os scripts CDN carregaram.

#### 2. Fontes não carregam
**Sintoma:** Texto em fonte padrão do sistema

**Solução:**
- Verifique conexão de internet
- Verifique se `<link rel="preconnect">` está presente
- Teste em modo anônimo (pode ser ad blocker)

#### 3. Layout quebrado em mobile
**Sintoma:** Elementos sobrepostos ou cortados

**Solução:**
- Use Chrome DevTools (F12) → Toggle device toolbar
- Teste em tamanhos reais: iPhone SE (375px), iPhone 14 (393px)
- Verifique se classes `md:` e `lg:` estão corretas

#### 4. Progress bar não move
**Sintoma:** Barra de progresso estática

**Solução:**
```javascript
// Verifique no console:
window.addEventListener('scroll', () => {
    console.log('Scrolling...');
});
```

Se não printar, JavaScript pode estar bloqueado ou erro anterior no código.

#### 5. CTAs não funcionam
**Sintoma:** Clique no botão não faz nada

**Solução:**
- Verifique se href está correto
- Para `mailto:`, certifique-se de que formato está correto
- Se usar JavaScript, verifique console por erros

### Debug Mode

Adicione no console para debug:

```javascript
// Mostrar todos os triggers GSAP
ScrollTrigger.getAll().forEach(st => {
    console.log(st);
});

// Testar scroll suave
document.querySelector('a[href="#preco"]').click();
```

## 📚 Recursos Adicionais

- **Design System:** [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)
- **Copy Original:** [copy.md](copy.md)
- **Tailwind Docs:** https://tailwindcss.com
- **GSAP Docs:** https://greensock.com/docs/
- **Lighthouse:** https://developers.google.com/web/tools/lighthouse
- **W3C Validator:** https://validator.w3.org/

## 📧 Contato

**Dúvidas ou sugestões sobre as landing pages:**
- Email: joao@example.com
- GitHub Issues: [Abrir issue](https://github.com/seu-repo/issues)

---

## 📋 Summary

### Páginas Disponíveis

| Página | Arquivo | Produto | Preço | Status |
|--------|---------|---------|-------|--------|
| Curso | `index.html` | Curso online | R$ 579/ano | ✅ Pronto |
| Livro | `prevenda.html` | Livro técnico | R$ 197 (pré-venda) | ✅ Pronto |

### Quick Start

```bash
# Servir localmente
cd web/
./serve.sh

# Acessar
# Curso: http://localhost:8000/index.html
# Livro: http://localhost:8000/prevenda.html
```

---

**Última atualização:** Novembro 2025  
**Versão:** 2.0  
**Autor:** João Gabriel Lima

**Status:**
- ✅ Landing Page Curso (index.html)
- ✅ Landing Page Livro - Pré-Venda (prevenda.html) ⭐ NOVO
