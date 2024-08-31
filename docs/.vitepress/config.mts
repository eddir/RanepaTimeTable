import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Расписание УЦП-23",
  description: "Скрипт для парсинга и автоматического обновления расписания вебинаров группы УЦП-23",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Главная', link: '/' },
      { text: 'ЧаВо', link: '/faq' }
    ],

    sidebar: [
      {
        text: 'Документация',
        items: [
          { text: 'Установка', link: '/install' },
          { text: 'Как это работает', link: '/faq' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/eddir/RanepaTimeTable' }
    ]
  }
})
