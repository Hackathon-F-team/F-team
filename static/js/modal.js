
  /*モーダルをコピペ。動くか確認*/
  /*htmlで宣言した要素を取得して、JS内で再度変数として宣言している*/
  const addChannelModal = document.getElementById("add-channel-modal");
  const deleteChannelModal = document.getElementById("delete-channel-modal");
  
  const addPageButtonClose = document.getElementById("add-page-close-btn");
  const deletePageButtonClose = document.getElementById("delete-page-close-btn");
  
  const addChannelBtn = document.getElementById("add-channel-btn");
  
  const addChannelConfirmBtn = document.getElementById(
    "add-channel-confirmation-btn"
  );
  const deleteChannelConfirmBtn = document.getElementById(
    "delete-channel-confirmation-btn"
  );
  //これで、必要な要素を取得してクリックイベントを発生させる準備ができた//
  
  
  
  
  
  // addChannelBtn[htmlでの<button id="add-channel-btn">チャンネル追加</button>ボタン]
  // がクリックされたら、modalOpen("add")という処理を行うという無名関数を定義
  addChannelBtn.addEventListener("click", () => {
    modalOpen("add");
  });
  
  
  // 上記のmodalOpen("add")などの関数を定義する。modeごとに異なる処理//
  // display = "block" で表示させると言う意味//
  // 具体的にはチャンネル追加モーダル、チャンネル削除モーダル、チャンネル変更モーダルのそれぞれを開く関数を定義している//
  function modalOpen(mode) {
    if (mode === "add") {
      addChannelModal.style.display = "block";
    } else if (mode === "delete") {
      deleteChannelModal.style.display = "block";
    } else if (mode === "update") {
      updateChannelModal.style.display = "block";
    }
  }
  
  // モーダル内のバツ印がクリックされた時はmodalClose("add")という処理を行う無名関数を定義//
  addPageButtonClose.addEventListener("click", () => {
    modalClose("add");
  });
  deletePageButtonClose.addEventListener("click", () => {
    modalClose("delete");
  });
  
  
  
  // 上記のmodalClose("add")などの関数を定義する。modeごとに異なる処理//
  // display = "none" で非表示にするという意味//
  // 具体的にはチャンネル追加モーダル、チャンネル削除モーダル、チャンネル変更モーダルのそれぞれを閉じる関数を定義している//
  function modalClose(mode) {
    if (mode === "add") {
      addChannelModal.style.display = "none";
    } else if (mode === "delete") {
      deleteChannelModal.style.display = "none";
    } else if (mode === "update") {
      updateChannelModal.style.display = "none";
    }
  }
  
  
  
  
  // 「要素がない」つまり「モーダルコンテンツ以外」がクリックされた時は、outsiderCloseという関数を定義して実行する//
  // 具体的にはチャンネル追加モーダル、チャンネル削除モーダルのいずれかを閉じる関数を作成して、実行している//
  //上の処理では二つに分けていた処理を同時に実行する書き方にされているだけ//
  addEventListener("click", outsideClose);
  function outsideClose(e) {
    if (e.target == addChannelModal) {
      addChannelModal.style.display = "none";
    } else if (e.target == deleteChannelModal) {
      deleteChannelModal.style.display = "none";
    }
  }

  

