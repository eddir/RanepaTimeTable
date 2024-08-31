<script setup>

import { ref } from 'vue';

const location = ref(window.location);
const calendarUrl = ref(`${location.value.origin}/c/timetable.ics`);

</script>

# Установка

Какой календарь использовать?

- [Google Календарь](#google-календарь)
- [Яндекс.Календарь](#yandex-календарь)
- [Другие календари](#другие-календари)

## Google Календарь

1. Перейдите на [страницу установки календаря](https://calendar.google.com/calendar/u/0/r/settings/addbyurl).
2. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}
```

3. Нажмите "Добавить календарь".

## Яндекс.Календарь

1. Перейдите на [страницу установки календаря](https://calendar.yandex.ru/import).
2. Выберите "По ссылке"
3. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}
```

4. Нажмите "Добавить".

## Другие календари

1. Откройте календарь.
2. Найдите пункт "Добавить календарь по ссылке".
3. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}
```

4. Нажмите "Добавить".


