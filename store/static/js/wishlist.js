var updatewishBtn = document.getElementsByClassName("update-wishlist");
for (i = 0; i < updatewishBtn.length; i++) {
  updatewishBtn[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "action:", action, "user:", user);
    if (user === "AnonymousUser") {
      window.location.href = "login/";
      console.log("not loged in");
    } else {
      updateUserWishlist(productId, action);
    }
  });
}
function updateUserWishlist(productId, action) {
  console.log("loged in sending data to wishlist");
  var url = "/update_wishlist/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId: productId,
      action: action,
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
