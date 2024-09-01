import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Расписание УЦП-23",
  description: "Скрипт для парсинга и автоматического обновления расписания вебинаров группы УЦП-23",
  locales: {
    root: {
      label: "Русский",
      lang: "ru",
      themeConfig: {
        search: {
          options: {
            translations: {
              button: {
                buttonText: "Искать",
                buttonAriaLabel: "Искать",
              },
              modal: {
                displayDetails: "Показать детали",
                resetButtonTitle: "Сброс",
                backButtonTitle: "Назад",
                noResultsText: "Ничего не найдено по запросу",
                footer: {
                  selectText: "Открыть",
                  selectKeyAriaLabel: "Открыть",
                  navigateText: "Навигация",
                  navigateUpKeyAriaLabel: "Выше",
                  navigateDownKeyAriaLabel: "Ниже",
                  closeText: "Закрыть",
                  closeKeyAriaLabel: "Закрыть",
                },
              },
            },
          },
        },
        lastUpdated: {
          text: "Обновлено",
        },
        outline: {
          label: "На этой странице",
        },
        docFooter: {
          prev: "Предыдущая страница",
          next: "Следующая страница",
        },
        darkModeSwitchLabel: "Тема",
        lightModeSwitchTitle: "Переключиться на светлую тему",
        darkModeSwitchTitle: "Переключиться на тёмную тему",
        sidebarMenuLabel: "Меню",
        returnToTopLabel: "Наверх",

        footer: {
          message: "Опубликовано под лицензией MIT",
          copyright:
              'Создано <a href="https://github.com/eddir" target="_blank">@EdRostkov</a>',
        },
      },
    },
  },
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
    ],
  }
})
