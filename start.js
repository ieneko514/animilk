(function() {
  const xhr = new XMLHttpRequest();
  xhr.addEventListener("abort", function() { alert("XHR aborted."); });
  xhr.addEventListener("error", function() { alert("XHR failed."); });
  xhr.addEventListener("timeout", function() { alert("XHR timed out."); });
  xhr.addEventListener("load", function() {
    try
    {
      WebAssembly.instantiate(xhr.response, {
      }).then(function(x) {
        x.instance.exports.animilk_begin();
      });
    }
    catch (exc)
    {
      console.error(exc);
      alert("Wasm error.");
    }
  });
  xhr.open("GET", "./animilk_native.wasm");
  xhr.responseType = "arraybuffer";
  xhr.send();
})();
