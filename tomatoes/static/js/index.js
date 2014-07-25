$(document).ready(function() {

    var myApiKey = 'gawtrve9bug4phrmzdfrqgc7';
//    var movieInfo = {};


    var getMovie = function () {
        var movieContainer = $('.movieInfoContainer');
        movieContainer.html(" ");
        var searchQuery = $('#searchMovies').val();
        var pageLimit = $('#arrayLimit').val();
        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
                'movies.json?apikey=' + myApiKey + '&q=' +
                searchQuery + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function (movie_response) {
                console.log(movie_response);
                var movies = movie_response.movies;
                console.log(movies);

                var movie_list = [];
                for ( var i = 0; i < movies.length; i++) {
                    var movie = movies[i];
                    var movieInfo = {};
                    var moreInformation = $('moreInformation');
                    movieInfo.title = movie.title;
                    movieInfo.release_year = movie.year;
                    movieInfo.critic_rating = movie.ratings.critics_score;
                    movieInfo.poster = movie.posters.original;
                    movieInfo.mpaa_rating = movie.mpaa_rating;
                    movieInfo.runtime = movie.runtime;
                    movieInfo.year = movie.year;
                    movieInfo.audience_score = movie.ratings.audience_score;
                    movie_list.push(movieInfo);
                    $('.searchResults').append("<div class='movieItem'><img class='moviePoster'src="
                        +movieInfo.poster+
                        "><p class='movieTitle'>"
                        +movieInfo.title+
                        "</p><p class='movieScore'>Movie Score: "
                        +(movieInfo.critic_rating+movieInfo.audience_score)/2.0+
                        "</p><button class='favorite' data-id="
                        +i+">Favorite This Movie</button><button class='moreInfoBtn'>More Information</button>" +
                        "<div class='moreInfo' style='display:none;'>" +
                        "<p class='mpaaRating'>MPAA Rating: "+movieInfo.mpaa_rating+
                        "</p><p class='runtime'>Runtime: "+movieInfo.runtime+"</p></div></div>");


                }
                $('.moreInfoBtn').on('click', function () {
                    console.log('get the button');
                    $(this).text(function (i, text) {
                        return text === "More Information" ? "Less Information" : "More Information";
                    });
                    $(this).siblings('.moreInfo').toggle()
                });

                $('.favorite').on('click', function () {
                    console.log('got fav button');
                    var movie_id = $(this).data('id');
                    var movie = movie_list[movie_id];
                    $(this).html("<img src='http://sycamorecreekchurch.org/blog/wp-content/uploads/2012/12/Favorites-icon2.png' height=50 width 50>");
                    movieInfo = JSON.stringify(movie);
                    console.log(movieInfo);
                    $.ajax({
                        url: '/new_movie_html/',
                        type: 'POST',
                        dataType: 'html',
                        data: movieInfo,
                        success: function (movie_response) {
                            $('.favorites').html(movie_response);
                            console.log(movie_response);
                        },
                        error: function (error_response) {
                            console.log(error_response);
                        }
                    });


                });


            },

            error: function (error_response) {
                console.log(error_response);
            }

        });


    };


    $('#getMovie').on('click', getMovie);

//    $.ajax({
//        url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
//              'lists/movies/upcoming.json?apikey=' + myApiKey + '&q=' +
//               searchQuery + '&page_limit=' + pageLimit,
//        type: 'GET',
//        dataType: 'jsonp',
//       success: function(movie_response) {
//            console.log(movie_response);
//            var movie = movie_response.movies[0];
//            movieInfo.title = movie.title;
//            movieInfo.release_year = movie.year;
//            movieInfo.critic_rating = movie.ratings.critics_score;
//            movieInfo.poster = movie.posters.original;
//            movieInfo.mpaa_rating = movie.mpaa_rating;
//            movieInfo.runtime = movie.runtime;
//            movieInfo.audience_score = movie.ratings.audience_score;
//        },
//        error: function(error_response) {
//            console.log(error_response);
//        }
//    });
//
//
//
//
//
//    $.ajax({
//        url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
//              'lists/dvds/new_releases.json?apikey=' + myApiKey + '&q=' +
//               searchQuery + '&page_limit=' + pageLimit,
//        type: 'GET',
//        dataType: 'jsonp',
//       success: function(movie_response) {
//            console.log(movie_response);
//            var movie = movie_response.movies[0];
//            movieInfo.title = movie.title;
//            movieInfo.release_year = movie.year;
//            movieInfo.critic_rating = movie.ratings.critics_score;
//            movieInfo.poster = movie.posters.original;
//            movieInfo.mpaa_rating = movie.mpaa_rating;
//            movieInfo.runtime = movie.runtime;
//            movieInfo.audience_score = movie.ratings.audience_score;
//        },
//        error: function(error_response) {
//            console.log(error_response);
//        }
//    });

//    $('#saveMovieFavorite').on('click', function() {
//                movieInfo = JSON.stringify(movieInfo);
//                $.ajax({
//                    url: '/new_movie_json/',
//                    type: 'POST',
//                    dataType: 'json',
//                    data: movieInfo,
//                    success: function(movie_response) {
//                        console.log(movie_response);
//                    },
//                    error: function(error_response) {
//                        console.log(error_response);
//                    }
//                });
//            });

    $('#favorites').on('click', function () {

        $.ajax({
            url: '/view_favorites/',
            type: 'GET',

            dataType: 'html',

            success: function (response) {
                $('.searchResults').html(response);
                console.log(response);
                $('.removeFavorite').on('click', function(){
                    console.log('got button');

                    var movieTitle = $(this).data('title');
                    movieTitle = JSON.stringify(movieTitle);
                    $.ajax({
                        url:'/delete_favorite/',
                        type: 'POST',
                        dataType: 'html',
                        data: movieTitle,
                        success: function(response){
                            console.log(response);
                            console.log('delted')
                        },
                        error: function(error_response){
                            console.log(error_response);
                            console.log('fuck you')
                        }
                    })

                })

            },
            error: function () {
                console.log("fucked");
            }
        }).complete(function(){
                   $('#accordion').accordion({active: 1});

        });
    });


});
