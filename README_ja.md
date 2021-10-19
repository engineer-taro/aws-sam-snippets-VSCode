# aws-sam-snippets-VSCode

こちらのリポジトリは VSCode で SAM のテンプレートを快適に記述するために開発中のリポジトリです。
現在開発中のため、対応していない点が多くありますが、最低限の機能から徐々にプッシュしていく予定です。
また、CloudFormation の記述に関しては本リポジトリの対象としていないため、CloudFormation 専用の別拡張機能をご利用ください。

# 開発の進捗について

現在進捗はフェーズ 1 です。
機能追加の順序は以下を予定しています。

## フェーズ 1

Type: に続く記述をスニペットに追加。
Properties のプロパティ名までを対象とする。

## フェーズ 2

[EventSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventsource.html)など、頻繁に記述するものを対象にする。

## フェーズ 3

[CorsConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-corsconfiguration.html)頻繁に記述しないものを対象にする。
