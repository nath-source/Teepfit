const iframe = document.getElementById('myIframe');

iframe.addEventListener('mouseover', () => {
  const src = '(link unavailable)'; // replace VIDEO_ID with the actual video ID
  iframe.src = src;
});

iframe.addEventListener('mouseout', () => {
  iframe.src = '';
});
