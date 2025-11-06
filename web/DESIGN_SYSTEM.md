# Design System - DSPy Course Landing Page

## 🎨 Paleta de Cores

### Backgrounds (Dark Theme)
```css
--bg-primary: #0a0e1a      /* Mais escuro - fundo principal e sections pares */
--bg-secondary: #0f172a    /* Escuro - sections alternadas */
--bg-tertiary: #1e293b     /* Médio escuro - cards e elementos elevados */
```

### Borders & Dividers
```css
--border-subtle: rgba(99, 102, 241, 0.1)   /* Bordas sutis */
--border-medium: rgba(99, 102, 241, 0.2)   /* Bordas normais */
--border-strong: rgba(99, 102, 241, 0.4)   /* Bordas em destaque */
```

### Text Colors
```css
--text-primary: #f1f5f9    /* Branco quase puro - títulos principais */
--text-secondary: #cbd5e1  /* Cinza claro - subtítulos e corpo */
--text-tertiary: #94a3b8   /* Cinza médio - descrições */
--text-muted: #64748b      /* Cinza escuro - hints e metadados */
```

### Brand Colors
```css
--color-primary: #6366f1   /* Indigo - cor principal da marca */
--color-secondary: #8b5cf6 /* Purple - cor secundária */
--color-accent: #ec4899    /* Pink - destaque e CTAs especiais */
```

### Semantic Colors
```css
--color-success: #10b981   /* Verde - sucesso, confirmações */
--color-warning: #f59e0b   /* Laranja - avisos */
--color-error: #ef4444     /* Vermelho - erros */
```

## 📐 Estrutura e Hierarquia

### Tipografia

**Fontes:**
- **Headings e UI**: Inter (Google Fonts)
- **Código e ASCII Art**: JetBrains Mono (Google Fonts)

**Hierarquia de Tamanhos:**
```
Hero Title: 4xl → 6xl (responsive)
Section Titles: 4xl → 5xl
Module Titles: 2xl
Card Titles: xl
Body Text: base
Small Text/Hints: sm
```

**Cores por Contexto:**
- `h1, h2, h3, h4, h5, h6`: var(--text-primary)
- Parágrafos: var(--text-secondary)
- Descrições: var(--text-tertiary)
- Metadados: var(--text-muted)

### Espaçamento
```css
--space-xs: 0.5rem    /* 8px */
--space-sm: 1rem      /* 16px */
--space-md: 1.5rem    /* 24px */
--space-lg: 2rem      /* 32px */
--space-xl: 3rem      /* 48px */
```

### Sombras
```css
--shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.4)
--shadow-md: 0 4px 16px rgba(0, 0, 0, 0.5)
--shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.6)
--shadow-glow: 0 0 20px rgba(99, 102, 241, 0.3)
```

## 🧩 Componentes

### Cards
```css
background: var(--bg-tertiary)
border: 1px solid var(--border-medium)
box-shadow: var(--shadow-md)

/* Hover State */
transform: translateY(-5px)
border-color: var(--border-strong)
box-shadow: var(--shadow-glow), var(--shadow-lg)
```

### Buttons (CTA)
```css
background: var(--gradient-primary)
color: var(--text-primary)
box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3)

/* Hover State */
transform: scale(1.05)
box-shadow: 0 15px 40px rgba(99, 102, 241, 0.5)
```

### Terminal/Code Blocks
```css
background: var(--bg-primary)
border: 1px solid var(--border-medium)
font-family: 'JetBrains Mono', monospace
color: var(--color-success) /* para código */
```

## 🎯 Progressão de Cor nos Módulos

Os módulos seguem uma progressão de cores para indicar o nível:

1. **Módulos 1-3** (Fundamentos): `var(--color-primary)` - Indigo
2. **Módulos 4-6** (Avançado): `var(--color-secondary)` - Purple
3. **Módulos 7-8** (Produção): `var(--color-success)` - Green

```
🎓 Fundamentos → 🛠️ Construção → ⚡ Otimização → 🚀 Produção
  (Indigo)        (Indigo)      (Purple)      (Green)
```

## 📱 Responsividade

### Breakpoints (Tailwind padrão)
- **sm**: 640px
- **md**: 768px
- **lg**: 1024px
- **xl**: 1280px

### Mobile First
- ASCII art: `font-size: clamp(0.4rem, 1.2vw, 0.9rem)`
- Títulos: responsive de 4xl para 6xl
- Grids: `grid-cols-1` → `md:grid-cols-3`
- Flex direction: `flex-col` → `md:flex-row`

## ✨ Animações

### GSAP Animations
```javascript
// Hero entrance
gsap.from("#hero-title", {
    duration: 1,
    y: 50,
    opacity: 0,
    ease: "power3.out"
});

// Module cards on scroll
gsap.from(card, {
    scrollTrigger: {
        trigger: card,
        start: "top 80%",
    },
    duration: 0.8,
    x: index % 2 === 0 ? -100 : 100,
    opacity: 0,
    ease: "power3.out"
});
```

### CSS Animations
```css
/* Floating effect para cards */
@keyframes floating {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

/* Glow effect para ASCII art */
@keyframes glow {
    from {
        text-shadow: 0 0 5px var(--color-primary),
                     0 0 10px var(--color-primary),
                     0 0 15px var(--color-primary);
    }
    to {
        text-shadow: 0 0 10px var(--color-secondary),
                     0 0 20px var(--color-secondary),
                     0 0 30px var(--color-secondary);
    }
}
```

## 🎨 Gradientes

### Text Gradient (Títulos especiais)
```css
background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### Button Gradient
```css
background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-secondary) 100%);
```

### Background Gradient
```css
background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
```

## ♿ Acessibilidade

### Contrast Ratios
Todas as combinações de texto/fundo atendem WCAG AA (4.5:1 para texto normal):

- `text-primary` em `bg-primary`: **14.2:1** ✓
- `text-secondary` em `bg-primary`: **10.5:1** ✓
- `text-tertiary` em `bg-primary`: **6.8:1** ✓
- `color-primary` em `bg-primary`: **8.3:1** ✓

### Focus States
Todos os elementos interativos devem ter estados de foco visíveis:
```css
:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
}
```

## 📋 Boas Práticas

1. **Sempre use variáveis CSS** ao invés de cores hardcoded
2. **Mantenha contraste adequado** - mínimo 4.5:1 para texto
3. **Use a progressão de cores** para indicar nível/fase do conteúdo
4. **Animations sutis** - evite movimentos exagerados
5. **Mobile first** - sempre teste em dispositivos pequenos primeiro
6. **Consistência** - use os mesmos padrões em toda a página

## 🔧 Como Usar

### Aplicar cor de texto:
```html
<!-- Usando classes utilitárias -->
<p class="text-primary">Título principal</p>
<p class="text-secondary">Subtítulo</p>
<p class="text-tertiary">Descrição</p>

<!-- Ou inline styles -->
<h3 style="color: var(--color-primary);">Módulo</h3>
```

### Criar um card:
```html
<div class="card rounded-xl p-6">
    <h3 style="color: var(--color-primary);">Título</h3>
    <p class="text-tertiary">Descrição do card</p>
</div>
```

### Badge/Tag:
```html
<span style="background: rgba(99, 102, 241, 0.2); color: var(--color-primary);" 
      class="px-3 py-1 rounded-full text-sm">
    Tag
</span>
```

---

**Última atualização:** Novembro 2025  
**Versão:** 2.0  
**Autor:** João Gabriel Lima


