const stripe = Stripe("pk_test_DqQUuc8rpMvYCyWFJlgGzTOz00SRUcK8nF");
let session_id = JSON.parse(document.getElementById('session-data').textContent);

$('#payNow').click(() => {
  stripeCheckout();
});

async function stripeCheckout() {
  const {error} = await stripe.redirectToCheckout({
    sessionId: session_id
  });

  if (error) {
    console.log('Something went wrong!');
  }
}

