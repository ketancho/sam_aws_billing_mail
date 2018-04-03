### Overview
* AWS の利用料金を日次でメール通知します。
* AWS Serverless Application Model を用いて実装しており、コマンドひとつで導入することができます。

### Usage

1. SAM のセットアップが完了している前提です。もしセットアップがまだであれば、[こちら](http://www.ketancho.net/entry/2017/12/25/030849)をご覧ください。
2. `template.yaml` の `MAIL_FROM` , `MAIL_TO` を変更してください。(Gmailでしか動作確認しておりません。）
3. `sh deploy.sh` コマンドを実行してください。
4. 初回実行時にメールアドレスの verify が必要です。構築された Lambda Function を実行してください。2. で設定したメールアドレスに、verifyメールが送信されるので、承認してください。
5. 以上で設定完了です。日時でメールが送信されます。


## Author

[@ketancho](https://twitter.com/ketancho)
