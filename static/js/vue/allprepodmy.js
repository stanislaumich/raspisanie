      const url = "http://127.0.0.1:8000/api/person/1/";

	  const vm = new Vue({
              el: '#app',
              //Mock data for the value of BTC in USD

                          data: {
          results: []
        },
        mounted() {
          axios.get(url).then(response => {
            this.results = response.data
          })
        }
      });
