var Animal = {
  type: "Invertebrados",
  displayType: function () {
    console.log(this.type);
  },
};

var animal1 = Object.create(Animal);
animal1.displayType();

var pescado = Object.create(Animal);
pescado.type = "Pescados";
pescado.displayType();
