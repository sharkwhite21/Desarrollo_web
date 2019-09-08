

//DOM
/*
let Links = document.querySelectorAll("a");

Links.forEach(function(link){
  console.log(link);
});
*/
//obtener los elementos de la clase .close
let Close = document.querySelectorAll(".close");

//recorrelos
Close.forEach(function(close){
  close.addEventListener("click",function(Ev){
    Ev.preventDefault();
    let Content = document.querySelector(".content");

    //Quitarle la animacion que ya tiene
    Content.classList.remove("fadeInDown");
    Content.classList.remove("animated");

    //colocarle  para animar su salida
    Content.classList.add("fadeOutUp");
    Content.classList.add("animated");

    //tarde en redireccionar al home

    setTimeout(function(){
      location.href = "/Boletines";
    },1000);

    /*
    este se estara haciendo contantementecada 1 sec.
    setInterval(function(){
      location.href = "/";
    },1000);*/
    return False;
  });
  //console.log(span);
});

//Agregar un evento a cada uno de ellos.
