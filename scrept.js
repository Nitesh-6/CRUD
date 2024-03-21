fetch("http://127.0.0.1:5003/products")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    data = data.products;
    data.map((product) => console.log(product.name));
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });
