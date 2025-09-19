from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Watermark Bot — Made by Ankit Shakya</title>
  <style>
    :root{
      --red-rose: #C72C48;   /* red-rose */
      --navy-blue: #0B2545;  /* navy-blue */
      --bg: #f7f8fb;
      --card: #ffffff;
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg, #fcfdff 0%, #f0f4fb 100%);
      color: #0B2545;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      padding:28px;
      display:flex;
      min-height:100vh;
      align-items:flex-start;
      justify-content:center;
    }

    .wrap{
      width:100%;
      max-width:980px;
      background:var(--card);
      border-radius:16px;
      box-shadow:0 10px 30px rgba(11,37,69,0.08);
      padding:22px;
      border-top:6px solid var(--red-rose);
      overflow:hidden;
    }

    header{
      display:flex;
      gap:16px;
      align-items:center;
      margin-bottom:18px;
    }
    .logo{
      width:58px;
      height:58px;
      border-radius:12px;
      background:linear-gradient(135deg,var(--red-rose),var(--navy-blue));
      display:flex;
      align-items:center;
      justify-content:center;
      color:white;
      font-weight:700;
      font-size:16px;
      box-shadow:0 6px 18px rgba(199,44,72,0.18);
    }
    h1{margin:0;font-size:20px}
    p.lead{margin:0;color: #33415a; font-size:13px}

    .grid{
      display:grid;
      grid-template-columns: 360px 1fr;
      gap:18px;
      margin-top:16px;
    }

    /* left controls */
    .panel{
      background:linear-gradient(180deg,#fff,#fbfdff);
      border-radius:12px;
      padding:14px;
      border:1px solid rgba(11,37,69,0.04);
    }
    label{display:block;font-size:13px;color:#233047;margin-bottom:8px}
    input[type="file"]{display:block;margin-bottom:12px}
    .field{margin-bottom:12px}
    input[type="text"], select, input[type="number"], input[type="range"]{
      width:100%;
      padding:8px 10px;
      border-radius:8px;
      border:1px solid rgba(11,37,69,0.08);
      font-size:14px;
      background:white;
    }
    .row{display:flex;gap:8px}
    .btn{
      display:inline-block;
      padding:10px 12px;
      border-radius:10px;
      background:var(--navy-blue);
      color:white;
      border:none;
      cursor:pointer;
      font-weight:600;
      font-size:14px;
      box-shadow:0 6px 14px rgba(11,37,69,0.08);
    }
    .btn.ghost{
      background:transparent;
      color:var(--navy-blue);
      border:1px solid rgba(11,37,69,0.08);
      font-weight:600;
    }

    /* preview */
    .preview-card{
      background:linear-gradient(180deg,#ffffff,#fbfdff);
      border-radius:12px;
      padding:12px;
      border:1px solid rgba(11,37,69,0.04);
      display:flex;
      flex-direction:column;
      gap:10px;
    }
    .canvas-wrap{
      background:linear-gradient(180deg,#eef4ff, #f8fafc);
      border-radius:10px;
      padding:12px;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:360px;
      position:relative;
      overflow:hidden;
    }
    canvas{
      max-width:100%;
      max-height:100%;
      border-radius:6px;
      background:#e9eef7;
    }

    .note{font-size:12px;color:#4b5a73}
    footer.controls{display:flex;gap:10px;align-items:center;justify-content:flex-end;margin-top:6px}

    .small{font-size:12px;color:#5b6b85}
    .pos-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
    .pos-grid button{padding:8px;border-radius:8px;border:1px solid rgba(11,37,69,0.06);background:white;cursor:pointer}
    .pos-grid button.active{outline:2px solid var(--red-rose)}
    .tag{
      display:inline-flex;
      gap:8px;
      align-items:center;
      background:linear-gradient(90deg, rgba(199,44,72,0.06), rgba(11,37,69,0.04));
      padding:8px 12px;border-radius:999px;color:var(--navy-blue);
      font-weight:600;
    }

    /* responsive */
    @media (max-width:880px){
      .grid{grid-template-columns:1fr; }
      .panel{order:2}
      .preview-card{order:1}
    }
  </style>
</head>
<body>
  <div class="wrap" role="main">
    <header>
      <div class="logo">AS</div>
      <div>
        <h1>Watermark Bot</h1>
        <p class="lead">Quickly add a watermark — <span class="tag">Made by Ankit Shakya</span></p>
      </div>
    </header>

    <div class="grid">
      <!-- left: controls -->
      <div class="panel" aria-label="Controls">
        <label for="file">Choose an image</label>
        <input id="file" type="file" accept="image/*" />

        <div class="field">
          <label for="wmText">Watermark text</label>
          <input id="wmText" type="text" value="Made by Ankit Shakya" />
        </div>

        <div class="field">
          <label>Font size (px)</label>
          <input id="fontSize" type="number" min="10" max="200" value="28" />
        </div>

        <div class="field">
          <label>Opacity</label>
          <input id="opacity" type="range" min="0" max="1" step="0.01" value="0.6" />
        </div>

        <div class="field">
          <label>Color</label>
          <select id="wmColor">
            <option value="#ffffff">White</option>
            <option value="#000000">Black</option>
            <option value="#C72C48" selected>Red Rose</option>
            <option value="#0B2545">Navy Blue</option>
          </select>
        </div>

        <div class="field">
          <label>Position</label>
          <div class="pos-grid" id="posGrid">
            <button data-pos="tl">Top-left</button>
            <button data-pos="tc">Top-center</button>
            <button data-pos="tr">Top-right</button>
            <button data-pos="ml">Middle-left</button>
            <button data-pos="mc" class="active" data-pos="mc">Center</button>
            <button data-pos="mr">Middle-right</button>
            <button data-pos="bl">Bottom-left</button>
            <button data-pos="bc">Bottom-center</button>
            <button data-pos="br">Bottom-right</button>
          </div>
        </div>

        <div class="field">
          <label>Rotation (degrees)</label>
          <input id="rotation" type="number" min="-90" max="90" value="0" />
        </div>

        <div style="display:flex;gap:8px;margin-top:6px">
          <button id="applyBtn" class="btn">Apply Watermark</button>
          <button id="downloadBtn" class="btn ghost">Download</button>
        </div>

        <p class="note" style="margin-top:12px">Tip: For best results use high-resolution images. This runs entirely in your browser — no files are uploaded to any server.</p>
      </div>

      <!-- right: preview -->
      <div class="preview-card">
        <div style="display:flex;align-items:center;justify-content:space-between">
          <div><strong>Preview</strong><div class="small">See the watermark applied live</div></div>
          <div class="small">Format: PNG</div>
        </div>
        <div class="canvas-wrap" id="canvasWrap">
          <canvas id="canvas" width="800" height="450" aria-label="Preview canvas"></canvas>
        </div>

        <footer class="controls">
          <div class="small">Background colors: <span style="display:inline-block;width:14px;height:14px;background:var(--navy-blue);border-radius:3px;margin-left:8px;margin-right:6px"></span><span style="display:inline-block;width:14px;height:14px;background:var(--red-rose);border-radius:3px;margin-right:6px"></span></div>
        </footer>
      </div>
    </div>
  </div>

  <script>
    // Elements
    const fileInput = document.getElementById('file');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d', { alpha: true });
    const wmText = document.getElementById('wmText');
    const fontSizeInput = document.getElementById('fontSize');
    const opacityInput = document.getElementById('opacity');
    const wmColor = document.getElementById('wmColor');
    const applyBtn = document.getElementById('applyBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const rotationInput = document.getElementById('rotation');
    const posGrid = document.getElementById('posGrid');

    let img = new Image();
    let currentPos = 'mc';

    // position buttons
    posGrid.addEventListener('click', (e) => {
      if (e.target.tagName !== 'BUTTON') return;
      posGrid.querySelectorAll('button').forEach(b=>b.classList.remove('active'));
      e.target.classList.add('active');
      currentPos = e.target.getAttribute('data-pos');
      drawPreview();
    });

    // load image
    fileInput.addEventListener('change', (ev) => {
      const f = ev.target.files && ev.target.files[0];
      if (!f) return;
      const url = URL.createObjectURL(f);
      img = new Image();
      img.onload = () => {
        // set canvas size proportional to image but limit max width for display
        const maxW = 1200; // in case of huge images
        const ratio = img.width / img.height;
        let w = img.width;
        let h = img.height;
        if (w > maxW) {
          w = maxW;
          h = Math.round(w / ratio);
        }
        canvas.width = w;
        canvas.height = h;
        drawPreview();
        URL.revokeObjectURL(url);
      };
      img.src = url;
    });

    // draw preview + watermark
    function drawPreview() {
      // clear
      ctx.clearRect(0,0,canvas.width,canvas.height);
      // draw image (centered fit)
      if (img && img.complete && img.width) {
        // draw original image scaled to canvas size
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      } else {
        // placeholder
        ctx.fillStyle = '#eef4ff';
        ctx.fillRect(0,0,canvas.width,canvas.height);
        ctx.fillStyle = '#7b8aa3';
        ctx.font = '18px sans-serif';
        ctx.fillText('No image loaded. Choose an image to begin.', 16, 40);
      }

      // watermark values
      const text = wmText.value || 'Made by Ankit Shakya';
      const fontSize = parseInt(fontSizeInput.value) || 28;
      const opacity = parseFloat(opacityInput.value);
      const color = wmColor.value || '#C72C48';
      const rotation = parseFloat(rotationInput.value) || 0;

      // style
      ctx.save();
      ctx.globalAlpha = opacity;
      ctx.textBaseline = 'middle';
      ctx.textAlign = 'left';

      // pick font scaled to canvas
      const scale = canvas.width / 800; // baseline
      const adjustedFont = Math.max(10, Math.round(fontSize * scale));
      ctx.font = `${adjustedFont}px "Segoe UI", Roboto, Arial, sans-serif`;

      // measure text
      const metrics = ctx.measureText(text);
      const textWidth = metrics.width;
      const textHeight = adjustedFont;

      // determine position
      const margin = Math.round(14 * scale);
      let x = margin;
      let y = margin;

      switch(currentPos){
        case 'tl': x = margin; y = margin + textHeight/2; break;
        case 'tc': x = (canvas.width - textWidth)/2; y = margin + textHeight/2; break;
        case 'tr': x = canvas.width - textWidth - margin; y = margin + textHeight/2; break;
        case 'ml': x = margin; y = (canvas.height)/2; break;
        case 'mc': x = (canvas.width - textWidth)/2; y = (canvas.height)/2; break;
        case 'mr': x = canvas.width - textWidth - margin; y = (canvas.height)/2; break;
        case 'bl': x = margin; y = canvas.height - margin - textHeight/2; break;
        case 'bc': x = (canvas.width - textWidth)/2; y = canvas.height - margin - textHeight/2; break;
        case 'br': x = canvas.width - textWidth - margin; y = canvas.height - margin - textHeight/2; break;
      }

      // rotation and drop shadow
      ctx.translate(x + textWidth/2, y);
      ctx.rotate((rotation * Math.PI) / 180);
      ctx.translate(-(x + textWidth/2), -y);

      // shadow for readability
      ctx.fillStyle = 'rgba(0,0,0,0.24)';
      ctx.fillText(text, x+1, y+1);

      ctx.fillStyle = color;
      ctx.fillText(text, x, y);

      ctx.restore();
    }

    // apply (re-draw with latest values)
    applyBtn.addEventListener('click', () => {
      if (!img || !img.complete || !img.width) {
        alert('Please load an image first.');
        return;
      }
      drawPreview();
      // small visual feedback
      applyBtn.textContent = 'Applied ✓';
      setTimeout(()=> applyBtn.textContent = 'Apply Watermark', 900);
    });

    // live updates
    [wmText, fontSizeInput, opacityInput, wmColor, rotationInput].forEach(el=>{
      el.addEventListener('input', drawPreview);
    });

    // download function
    downloadBtn.addEventListener('click', () => {
      if (!img || !img.complete || !img.width) {
        alert('No image to download. Load and apply a watermark first.');
        return;
      }
      drawPreview();
      // create blob and download
      canvas.toBlob(blob=>{
        const a = document.createElement('a');
        const fname = `watermarked_${Date.now()}.png`;
        a.href = URL.createObjectURL(blob);
        a.download = fname;
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(a.href);
      }, 'image/png');
    });

    // initial placeholder draw
    (function init(){
      canvas.width = 800;
      canvas.height = 450;
      drawPreview();
    })();
  </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
