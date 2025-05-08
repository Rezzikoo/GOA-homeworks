function sharePrice(invested, changes) {
  const finalPrice = changes.reduce((acc, change) => acc * (1 + change / 100), invested);
  return finalPrice.toFixed(2);
}
