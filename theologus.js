/**
 * Theologus Plugin
 * Um assistente de perguntas e respostas teológicas.
 */
(function () {
  'use strict';

  var respostas = [
    {
      palavras: ['deus', 'existência', 'existe', 'criador'],
      resposta:
        'A existência de Deus é um dos temas centrais da teologia. Argumentos como o cosmológico, o ontológico e o teleológico foram desenvolvidos ao longo dos séculos por filósofos como Tomás de Aquino e Anselmo de Cantuária.',
    },
    {
      palavras: ['bíblia', 'escritura', 'livro sagrado', 'palavra'],
      resposta:
        'A Bíblia é composta de 66 livros no cânon protestante (73 no cânon católico), divididos em Antigo e Novo Testamento. É considerada a Palavra de Deus e o principal documento da fé cristã.',
    },
    {
      palavras: ['jesus', 'cristo', 'messias', 'filho de deus'],
      resposta:
        'Jesus Cristo é o centro da fé cristã. Ele é confessado como Filho de Deus, plenamente humano e plenamente divino, que viveu, morreu e ressuscitou para a salvação da humanidade.',
    },
    {
      palavras: ['salvação', 'salvo', 'redenção', 'redentor'],
      resposta:
        'Salvação, na teologia cristã, é a libertação do pecado e suas consequências, concedida por graça mediante a fé em Jesus Cristo. O conceito envolve justificação, santificação e glorificação.',
    },
    {
      palavras: ['pecado', 'mal', 'pecados', 'original'],
      resposta:
        'O pecado, na visão bíblica, é a transgressão da lei de Deus. O pecado original — a queda de Adão e Eva — afetou toda a humanidade. A teologia cristã ensina que Cristo é a solução para o problema do pecado.',
    },
    {
      palavras: ['espírito', 'espírito santo', 'paracleto', 'consolador'],
      resposta:
        'O Espírito Santo é a terceira pessoa da Santíssima Trindade. Ele guia, consola, convence de pecado e capacita os crentes para a vida cristã e para o testemunho.',
    },
    {
      palavras: ['trindade', 'trino', 'pai filho espírito'],
      resposta:
        'A doutrina da Trindade afirma que há um só Deus em três pessoas distintas: Pai, Filho e Espírito Santo. É um dos dogmas fundamentais do cristianismo histórico.',
    },
    {
      palavras: ['oração', 'orar', 'rezar', 'reza'],
      resposta:
        'A oração é a comunicação do crente com Deus. Na tradição cristã, inclui adoração, confissão, ação de graças e súplica. Jesus ensinou o "Pai Nosso" como modelo de oração.',
    },
    {
      palavras: ['igreja', 'congregação', 'comunidade', 'corpo de cristo'],
      resposta:
        'A Igreja é o corpo de Cristo — a comunidade dos crentes chamados por Deus. Ela tem missão de adorar, ensinar, crescer na fé e proclamar o Evangelho ao mundo.',
    },
    {
      palavras: ['batismo', 'batizar', 'água'],
      resposta:
        'O batismo é um rito central do cristianismo, simbolizando morte ao pecado e nova vida em Cristo. As tradições variam quanto à forma (imersão, aspersão, infusão) e ao sujeito (crentes ou infantes).',
    },
    {
      palavras: ['ceia', 'eucaristia', 'comunhão', 'mesa'],
      resposta:
        'A Ceia do Senhor (Eucaristia/Comunhão) é um sacramento instituído por Jesus na última ceia. As tradições cristãs diferem quanto à presença de Cristo no ato, mas concordam em sua importância como memória e proclamação da morte de Cristo.',
    },
    {
      palavras: ['fé', 'crer', 'crença', 'confiar'],
      resposta:
        'A fé, na teologia reformada, é um dom de Deus que envolve conhecimento (notitia), assentimento (assensus) e confiança (fiducia) em Cristo. É pela fé que o crente é justificado diante de Deus.',
    },
    {
      palavras: ['graça', 'misericórdia', 'favor imerecido'],
      resposta:
        'Graça é o favor imerecido de Deus para com os pecadores. A teologia cristã distingue graça comum (benefícios gerais a toda criação) de graça especial ou salvífica (concedida aos eleitos em Cristo).',
    },
    {
      palavras: ['escatologia', 'fim do mundo', 'volta', 'segunda vinda', 'apocalipse'],
      resposta:
        'A escatologia é o estudo das últimas coisas: morte, julgamento, céu e inferno, e a consumação de todas as coisas. A segunda vinda de Cristo é o grande horizonte da esperança cristã.',
    },
    {
      palavras: ['predestinação', 'eleição', 'escolhidos', 'calvino'],
      resposta:
        'A doutrina da predestinação ensina que Deus elegeu soberanamente, antes da fundação do mundo, aqueles que seriam salvos. Agostinho e Calvino são os principais expoentes desta doutrina no Ocidente cristão.',
    },
  ];

  var respostaGenerica =
    'Essa é uma questão teológica interessante! Posso ajudar com temas como: existência de Deus, Bíblia, Jesus Cristo, salvação, pecado, Espírito Santo, Trindade, oração, Igreja, batismo, Ceia do Senhor, fé, graça, escatologia e predestinação. Tente perguntar sobre um desses temas!';

  function normalizar(texto) {
    return texto
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '');
  }

  function buscarResposta(pergunta) {
    var normalizada = normalizar(pergunta);
    for (var i = 0; i < respostas.length; i++) {
      var item = respostas[i];
      for (var j = 0; j < item.palavras.length; j++) {
        if (normalizada.indexOf(normalizar(item.palavras[j])) !== -1) {
          return item.resposta;
        }
      }
    }
    return respostaGenerica;
  }

  function criarEstilos() {
    var style = document.createElement('style');
    style.textContent =
      '#theologus-btn{position:fixed;bottom:24px;right:24px;background:#3a5a8c;color:#fff;border:none;border-radius:50%;width:56px;height:56px;font-size:24px;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.3);z-index:9998;}' +
      '#theologus-box{display:none;position:fixed;bottom:92px;right:24px;width:320px;max-height:480px;background:#fff;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.2);z-index:9999;flex-direction:column;overflow:hidden;}' +
      '#theologus-header{background:#3a5a8c;color:#fff;padding:12px 16px;font-weight:bold;font-size:15px;display:flex;justify-content:space-between;align-items:center;}' +
      '#theologus-close{background:none;border:none;color:#fff;font-size:18px;cursor:pointer;line-height:1;}' +
      '#theologus-messages{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:8px;max-height:320px;}' +
      '.tg-msg-bot,.tg-msg-user{max-width:85%;padding:8px 12px;border-radius:12px;font-size:14px;line-height:1.5;}' +
      '.tg-msg-bot{background:#f0f4f8;color:#222;align-self:flex-start;border-bottom-left-radius:4px;}' +
      '.tg-msg-user{background:#3a5a8c;color:#fff;align-self:flex-end;border-bottom-right-radius:4px;}' +
      '#theologus-form{display:flex;border-top:1px solid #eee;padding:8px;}' +
      '#theologus-input{flex:1;border:1px solid #ccc;border-radius:8px;padding:8px 10px;font-size:14px;outline:none;}' +
      '#theologus-send{background:#3a5a8c;color:#fff;border:none;border-radius:8px;padding:8px 14px;margin-left:6px;cursor:pointer;font-size:14px;}';
    document.head.appendChild(style);
  }

  function adicionarMensagem(container, texto, tipo) {
    var div = document.createElement('div');
    div.className = tipo === 'user' ? 'tg-msg-user' : 'tg-msg-bot';
    div.textContent = texto;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
  }

  function iniciar() {
    criarEstilos();

    var btn = document.createElement('button');
    btn.id = 'theologus-btn';
    btn.title = 'Theologus — Assistente Teológico';
    btn.textContent = '✝';
    document.body.appendChild(btn);

    var box = document.createElement('div');
    box.id = 'theologus-box';
    box.innerHTML =
      '<div id="theologus-header">✝ Theologus<button id="theologus-close" title="Fechar">✕</button></div>' +
      '<div id="theologus-messages"></div>' +
      '<form id="theologus-form"><input id="theologus-input" type="text" placeholder="Faça uma pergunta teológica..." autocomplete="off"><button id="theologus-send" type="submit">Enviar</button></form>';
    document.body.appendChild(box);

    var messages = box.querySelector('#theologus-messages');
    var input = box.querySelector('#theologus-input');
    var form = box.querySelector('#theologus-form');
    var closeBtn = box.querySelector('#theologus-close');

    adicionarMensagem(
      messages,
      'Olá! Sou o Theologus, seu assistente teológico. Faça-me uma pergunta sobre teologia cristã!',
      'bot'
    );

    btn.addEventListener('click', function () {
      box.style.display = box.style.display === 'flex' ? 'none' : 'flex';
      if (box.style.display === 'flex') {
        input.focus();
      }
    });

    closeBtn.addEventListener('click', function () {
      box.style.display = 'none';
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var pergunta = input.value.trim();
      if (!pergunta) return;
      adicionarMensagem(messages, pergunta, 'user');
      input.value = '';
      var resposta = buscarResposta(pergunta);
      setTimeout(function () {
        adicionarMensagem(messages, resposta, 'bot');
      }, 300);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', iniciar);
  } else {
    iniciar();
  }
})();
