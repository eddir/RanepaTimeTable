<script setup>

const calendarUrl = "https://timetable.rostkov.me/c";

</script>

# Яндекс.Календарь

Выберите группу:

- [УЦП-23](#уцп-23)
- [УЦП-24](#уцп-24)

## УЦП-23

1. Перейдите на [страницу установки календаря](https://calendar.yandex.ru/import).
2. Выберите "По ссылке"
3. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}/timetable.ics
```

4. Нажмите "Добавить".

## УЦП-24

1. Перейдите на [страницу установки календаря](https://calendar.yandex.ru/import).
2. Выберите "По ссылке"
3. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}/up24.ics
```

4. Нажмите "Добавить".

