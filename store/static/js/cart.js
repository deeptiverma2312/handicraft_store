var updateBtn = document.getElementsByClassName("update-cart");
var popupBtn = document.getElementsByClassName("popup");

for (i = 0; i < popupBtn.length; i++) {
  popupBtn[i].addEventListener("click", function () {
    let modal = document.querySelector("#modal-pop");
    let image = document.querySelector(".pop-image");
    let title = document.querySelector(".pop-title");
    let price = document.querySelector(".pop-price");
    let size_select = document.querySelector("#size");
    let color_select = document.querySelector("#color");
    let material_select = document.querySelector("#material");
    let add_to_cart = document.querySelector(".add_to_cart");
    size_select.innerHTML = "";
    color_select.innerHTML = "";
    material_select.innerHTML = "";
    var productId = this.dataset.product;
    var urli = this.dataset.urli;
    var name = this.dataset.name;
    var pay_price = this.dataset.price;
    var size = this.dataset.size;
    var size_option = size.split(",");
    var color = this.dataset.color;
    var color_option = color.split(",");
    var material = this.dataset.material;
    var material_option = material.split(",");
    console.log(size_option);
    var action = this.dataset.action;

    console.log("productId:", productId, "action:", pay_price, "user:", user);
    if (user === "AnonymousUser") {
      window.location.replace("/login/");
      // window.location.href = "login/";
      console.log("not loged in");
    } else {
      modal.style.visibility = "visible";
      for (var i = 0; i < size_option.length; i++) {
        const newOption = document.createElement("option");
        const optionText = document.createTextNode(size_option[i]);
        // set option text
        newOption.appendChild(optionText);
        // and option value
        newOption.setAttribute("value", `${size_option[i]}`);
        size_select.appendChild(newOption);
      }
      for (var i = 0; i < color_option.length; i++) {
        const newOption = document.createElement("option");
        const optionText = document.createTextNode(color_option[i]);
        // set option text
        newOption.appendChild(optionText);
        // and option value
        newOption.setAttribute("value", `${color_option[i]}`);
        color_select.appendChild(newOption);
      }
      for (var i = 0; i < material_option.length; i++) {
        const newOption = document.createElement("option");
        const optionText = document.createTextNode(material_option[i]);
        // set option text
        newOption.appendChild(optionText);
        // and option value
        newOption.setAttribute("value", `${material_option[i]}`);
        material_select.appendChild(newOption);
      }
      add_to_cart.setAttribute("data-product", `${productId}`);
      add_to_cart.setAttribute("data-action", "add");
      image.src = urli;
      title.innerHTML = name;
      price.innerHTML = `Rs. ${pay_price}`;
    }
  });
}

for (i = 0; i < updateBtn.length; i++) {
  updateBtn[i].addEventListener("click", function (e) {
    var color = "";
    var size = "";
    var material = "";
    var productId = this.dataset.product;
    var action = this.dataset.action;
    if (e.target.classList.contains("add-btn")) {
      let size_select = document.querySelector("#size");
      let color_select = document.querySelector("#color");
      let material_select = document.querySelector("#material");

      var color = color_select.value;
      var size = size_select.value;
      var material = material_select.value;
    } else {
      var size = this.dataset.size;
      var color = this.dataset.color;
      var material = this.dataset.material;
    }

    console.log(
      "productId:",
      productId,
      "action:",
      action,
      "user:",
      user,
      "user:",

      "size:",
      size,
      "color:",
      color,
      "material:",
      material
    );
    if (user === "AnonymousUser") {
      window.location.href = "login/";
      console.log("not loged in");
    } else {
      updateUserOrder(productId, action, size, color, material);
    }
  });
}
function updateUserOrder(productId, action, size, color, material) {
  console.log("loged in sending data to cart");
  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId,
      action,
      size,
      color,
      material,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location = window.location.href;

      console.log(("data:", data));
    });
}
