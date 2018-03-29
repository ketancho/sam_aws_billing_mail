### Overview
* AWS の利用料金を日次でメール通知します
* AWS Serverless Application Model を用いて実装しており、簡単に導入することができます

### Usage

* SAM のセットアップが完了している前提です。もしセットアップがまだであれば、[こちら](http://www.ketancho.net/entry/2017/12/25/030849)をご覧ください。
* マネージドコンソールから、SESにメールアドレスを登録（verify）してください。
* そのメールアドレスを `template.yaml` に登録してください。（2箇所）
* `sh deploy.sh` コマンドを実行してください。

## Author

[@ketancho](https://twitter.com/ketancho)
