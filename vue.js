https://ru.vuejs.org/guide/essentials/template-syntax.html

Использование глобальной сборки
?

Указанная выше ссылка загружает глобальную сборку Vue, где все API 
верхнего уровня доступны как свойства глобального объекта Vue. 
Вот полный пример с использованием глобальной сборки:


<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<div id="app">{{ message }}</div>

<script>
  const { createApp, ref } = Vue

  createApp({
    setup() {
      const message = ref('Hello vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>



Использование сборки в виде ES-модуля
?

В остальной части документации в основном используется синтаксис ES-модулей.
 Большинство современных браузеров теперь поддерживают ES-модули нативно, 
 поэтому можно подключать Vue из CDN как нативный ES-модуль таким образом:
html

<div id="app">{{ message }}</div>

<script type="module">
  import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

  createApp({
    setup() {
      const message = ref('Привет Vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>

Использование Import maps
?

В примере выше импортируем по полному CDN URL, но дальше в документации увидим код, подобный этому:
js

import { createApp } from 'vue'

Чтобы импортировать в таком лаконичном формате нужно указать браузеру местоположение импорта vue с помощью Import Maps (карту импорта):
html

<script type="importmap">
  {
    "imports": {
      "vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
    }
  }
</script>

<div id="app">{{ message }}</div>

<script type="module">
  import { createApp, ref } from 'vue'

  createApp({
    setup() {
      const message = ref('Привет Vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>


