#esta es completada y no es pendiente, o rechazada, sintaxis alternativa

function dumy() {
  #si el tiempo es par o impar
  if (Math.floor(Date.now()/1000) % 2 == 0)
    return promise.resolve("Hola mundo");
  return promise.reject("Error");
}

dumy().then(console.log).catch(console.log); 
