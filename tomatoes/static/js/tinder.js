$(document).ready(function(){


   var myApiKey = 'gawtrve9bug4phrmzdfrqgc7';
    var resultsLimit = 5;


    $('.tinderBtn').on('click', function() {
        var searchQuery = $('#search').val();
        var pageLimit = 10;
        var movieId;

        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + myApiKey + '&q=' + searchQuery + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function (response){
                console.log(response);
                console.log(response.movies[0].id);
                movieId = response.movies[0].id;

            },
            error: function (response) {
                console.log(response);
            }
        }).complete(function(){
            $.ajax({
                url:'http://api.rottentomatoes.com/api/public/v1.0/movies/'+ movieId+ '/similar.json?apikey='+ myApiKey+'&limit=5',
                type: "GET",
                dataType: 'jsonp',
                success: function(response){
                    console.log(response);
                    for (var i =0; i <response.movies.length; i++){
                        var movieLink = response.movies[i].links.self;
                        $('#recommended').append("<div><p>"+response.movies[i].title+"<p><div class='synopsis'><button class='learnMore' data-link="+movieLink+">Learn More</button></div><button class='favoriteBtn'>Favorite</button></div>");
                        console.log(movieLink)
                    }
                },
                error: function(response){
                    console.log(response)
                }
            })
        });


    });


    $(document).on('click', '.learnMore', function (){
        var selfLink = $(this).data('link');
        var synopDest = $(this).parent().parent();
        $.ajax({
            url: selfLink + '?apikey=' + myApiKey,
            type: "GET",
            dataType: 'jsonp',
            success: function(response){
                console.log(response);
                console.log(response.synopsis);

                synopDest.append('<p>'+response.synopsis+'</p>');
                console.log(response.posters.original);
                synopDest.append("<img src='"+response.posters.original+"'>");


            },
            error: function(response){
                console.log(response)
            }
        })


    });
    $(document).on('click', '.favoriteBtn', function (){
                movieInfo = JSON.stringify(movieInfo);
                $.ajax({
                    url: '/new_favorite/',
                    type: 'POST',
                    dataType: 'json',
                    data: movieInfo,
                    success: function(response) {
                        console.log(response);
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            });





});