https://ru.vuejs.org/guide/essentials/template-syntax.html

������������� ���������� ������
?

��������� ���� ������ ��������� ���������� ������ Vue, ��� ��� API 
�������� ������ �������� ��� �������� ����������� ������� Vue. 
��� ������ ������ � �������������� ���������� ������:


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



������������� ������ � ���� ES-������
?

� ��������� ����� ������������ � �������� ������������ ��������� ES-�������.
 ����������� ����������� ��������� ������ ������������ ES-������ �������, 
 ������� ����� ���������� Vue �� CDN ��� �������� ES-������ ����� �������:
html

<div id="app">{{ message }}</div>

<script type="module">
  import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

  createApp({
    setup() {
      const message = ref('������ Vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>

������������� Import maps
?

� ������� ���� ����������� �� ������� CDN URL, �� ������ � ������������ ������ ���, �������� �����:
js

import { createApp } from 'vue'

����� ������������� � ����� ���������� ������� ����� ������� �������� �������������� ������� vue � ������� Import Maps (����� �������):
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
      const message = ref('������ Vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>


