axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";


var app = new Vue({
    el: '#idNewsListPage',
    data: {
        hideArticlesList: false // by default dont hide articles
    },
    methods: {
        reloadNews: function () {
            console.log('reload news');
            this.hideArticlesList = true;
            axios({
                method: 'get',
                baseURL: window.location.origin, //we need base url
                url: 'api/get_news/',
                responseType: 'json',
            })
                .then(async function (response) {
                    console.log('News reloaded Successfully');
                    location.reload();
                }.bind(this))

                .catch(function (error) {
                    console.log('News reload ERROR');
                    alert(error);
                });

        },
        articleClicked: function (url) {
            console.log('id=', url);
            window.location.href = url;
        }
    },

    delimiters: ["[[", "]]"],
});
