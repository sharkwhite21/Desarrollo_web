function GET(url) {
  return new Promise(function(resolve,reject){

    let ajaxCall = new XMLHttpRequest();
    //definimos que va abrir la pagina
    ajaxCall.open('Get',url);

    ajaxCall.onload = function() {
      //aqui esta si la promesa se resuelve o no.
      if(ajaxCall.status == 200) return resolve(ajaxCall.response);
      reject(Error(ajaxCall.status));
    };
    //definimos el error
    ajaxCall.onerror = function (err) {
      reject(err);
    }

    ajaxCall.send();
  });
}

function getUserInfo(username){
    return GET("https://api.github.com/users/"+username);
}

function getRepos(repos_url) {
  return GET(repos_url);
}

getUserInfo("codigofacilito").then(response => {
    let responseJSON = JSON.parse(response);

    console.log(responseJSON.repos_url);

    getRepos(responseJSON.repos_url).then( repos => {console.log(repos)});
}
).catch(console.log);
