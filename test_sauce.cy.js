describe("Sauce Demo - User Journeys", () => {
  beforeEach(() => {
    cy.visit("https://www.saucedemo.com/");
  });

  it("Happy Path: Login and Add to Cart", () => {
    cy.login("standard_user", "secret_sauce");
    cy.addProductToCart("Sauce Labs Backpack");
    cy.verifyCartCount(1);
    cy.viewCart();
    cy.verifyCartItem("Sauce Labs Backpack");
  });

  it("Sad Path: Invalid Login Credentials", () => {
    cy.login("locked_out_user", "secret_sauce");
    cy.get(".error-message")
      .should("be.visible")
      .and("contain", "Epic sadface: Sorry, this user has been locked out.");
  });

  it("Robustness: Empty Cart", () => {
    cy.login("standard_user", "secret_sauce");
    cy.checkCartIsEmpty();
    cy.addProductToCart("Sauce Labs Bike Light");
    cy.checkCartIsNotEmpty();
  });

  it("Feature: Filtering Products", () => {
    cy.login("standard_user", "secret_sauce");
    cy.filterProducts("Bike Light");
    cy.verifyFilteredProducts("Bike Light");
  });

  it("Thoroughness: Checkout Process (Partial)", () => {
    cy.login("standard_user", "secret_sauce");
    cy.addProductToCart("Sauce Labs Fleece Jacket");
    cy.viewCart();
    cy.get(".shopping_cart_link").click();
    cy.contains("CHECKOUT").should("be.visible").click();
  });
});

function login(username, password) {
  cy.get("#user-name").type(username);
  cy.get("#password").type(password);
  cy.get('[type="submit"]').click();
}

function addProductToCart(productName) {
  cy.contains(productName).siblings('[data-test="add-to-cart-button"]').click();
}

function verifyCartCount(expectedCount) {
  cy.get(".shopping_cart_badge").should("have.text", expectedCount.toString());
}

function viewCart() {
  cy.get('[data-test="shopping_cart"]').click();
}

function verifyCartItem(productName) {
  cy.get('[data-test="item-name"]').should("contain", productName);
}

function checkCartIsEmpty() {
  cy.get(".shopping_cart_badge").should("not.exist");
}

function checkCartIsNotEmpty() {
  cy.get(".shopping_cart_badge").should("exist");
}

function filterProducts(filterTerm) {
  cy.get("#search_text").type(filterTerm);
}

function verifyFilteredProducts(expectedTerm) {
  cy.get(".inventory_item").each(($el) => {
    cy.wrap($el)
      .find(".inventory_item_name")
      .invoke("text")
      .then((text) => {
        expect(text).to.include(expectedTerm);
      });
  });
}
