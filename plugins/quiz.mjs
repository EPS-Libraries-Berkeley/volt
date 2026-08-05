export const quizDirective = {
  name: 'multiple-choice',
  doc: 'Multiple choice quiz directive',
  arg: { type: String },
  options: {
    a: { type: String, required: true },
    b: { type: String, required: true },
    c: { type: String },
    correct: { type: String, required: true },
    explanation: { type: String }
  },
  run(data) {
    const qId = Math.random().toString(36).substring(2, 7);
    return [
      {
        type: 'html',
        value: `
          <div style="border: 1px solid #d0d7de; border-radius: 8px; padding: 18px; background: #ffffff; margin: 1.5em 0;">
            <p style="margin-top: 0; font-weight: 600;">${data.arg}</p>
            <div style="display: flex; flex-direction: column; gap: 8px; margin: 12px 0;">
              <label style="cursor: pointer;"><input type="radio" name="q_${qId}" value="a"> A) ${data.options.a}</label>
              <label style="cursor: pointer;"><input type="radio" name="q_${qId}" value="b"> B) ${data.options.b}</label>
              ${data.options.c ? `<label style="cursor: pointer;"><input type="radio" name="q_${qId}" value="c"> C) ${data.options.c}</label>` : ''}
            </div>
            <button onclick="
              const fb = document.getElementById('fb_${qId}');
              const sel = document.querySelector('input[name=q_${qId}]:checked');
              if(!sel) { fb.style.color='#d97706'; fb.innerHTML='⚠️ Please select an option.'; return; }
              if(sel.value === '${data.options.correct}') {
                fb.style.color = '#16a34a';
                fb.innerHTML = '✅ <b>Correct!</b> ${data.options.explanation || ''}';
              } else {
                fb.style.color = '#dc2626';
                fb.innerHTML = '❌ <b>Incorrect.</b> Try again!';
              }
            " style="background-color: #003262; color: white; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer;">
              Check Answer
            </button>
            <div id="fb_${qId}" style="margin-top: 10px; font-weight: 500;"></div>
          </div>
        `
      }
    ];
  }
};

// REQUIRED: Plugin export definition
const plugin = {
  name: 'VOLT Quiz Plugin',
  directives: [quizDirective]
};

export default plugin;