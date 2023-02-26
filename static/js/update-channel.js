/*htmlで宣言した要素を取得して、JS内で再度変数として宣言している*/
const updateButton = document.getElementById("channel-update");
const updateChannelModal = document.getElementById("update-channel-modal");
const updatePageButtonClose = document.getElementById("update-page-close-btn");
//これで、必要な要素を取得してクリックイベントを発生させる準備ができた//


//updateChannnelという関数をアロー関数式で定義している
//modal.jsで定義したmodal.Open("update")を使用している※チャンネル変更モーダルを表示する関数
//ユーザーIDがチャンネルIDと異なる場合は何もしない、同じ場合はmodal.Openを実行する
const updateChannel = () => {
  if (uid !== channel.uid) {
    return;
  } else {
    modalOpen("update");
  }
};


//updateButtonを押すとupdateChannnel関数を実行する無名関数を作成。
updateButton.addEventListener("click", updateChannel);





//updateButtonCloseを押すとmodalClose("update")を実行する無名関数を作成する。
updatePageButtonClose.addEventListener("click", () => {
  modalClose("update");
});