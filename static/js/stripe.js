// Code take from Stripe documentation @
// https://stripe.com/docs/payments/checkout/one-time#redirect-checkout
const stripe = Stripe("pk_test_DqQUuc8rpMvYCyWFJlgGzTOz00SRUcK8nF");

// Session id inserted by Django template as JSON
let session_id = JSON.parse(
  document.getElementById("session-data").textContent
);

async function stripeCheckout() {
  const { error } = await stripe.redirectToCheckout({
    sessionId: session_id
  });

  if (error) {
    console.log("Something went wrong!");
  }
}

// jQuery to connect button click to our function
$("#payNow").click(() => {
  stripeCheckout();
});
