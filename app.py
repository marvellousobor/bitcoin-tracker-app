<!doctype html>
<html lang="en">
  <head>
    <title>BTC–USD Tracker</title>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}"
    />
  </head>
  <body>
    <section class="btc-card">
      <h1>₿ Bitcoin (BTC)</h1>

      <p class="price">$ {{ price }}</p>

      <p class="change {{ 'up' if change > 0 else 'down' }}">
        24h Change: {{ change }}%
      </p>

      <p class="note">Updates on page refresh</p>
    </section>
  </body>
</html>
