<script setup>

const calendarUrl = "https://timetable.rostkov.me/c";

</script>

# Google Календарь

Выберите группу:

- [УЦП-23](#уцп-23)
- [УЦП-24](#уцп-24)

## УЦП-23

1. Перейдите на [страницу установки календаря](https://calendar.google.com/calendar/u/0/r/settings/addbyurl).
2. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}/timetable.ics
```

3. Нажмите "Добавить календарь".

## УЦП-24

1. Перейдите на [страницу установки календаря](https://calendar.google.com/calendar/u/0/r/settings/addbyurl).
2. Введите адрес календаря:

```plaintext-vue
{{ calendarUrl }}/up24.ics
```

3. Нажмите "Добавить календарь".

