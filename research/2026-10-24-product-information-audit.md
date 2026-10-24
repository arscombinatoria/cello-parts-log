# 製品情報の不足・確認状況の横断調査（2026年10月24日）

調査基準はデフォルトブランチ `main` の `e58e9a2c931bd79b461c2335d1dad2cb9fb93c48`。取得後に fast-forward で同期した。時刻・日付は日本時間を基準とする。対象は `docs/**/*.{md,mdx}` 全45ファイル（md 45、mdx 0）。`AGENTS.md` と `.agents/skills/japanese-tech-writing/SKILL.md` を読んでから編集した。

## 集計方法と範囲

指定語の検索結果は、未指定31回、未確認9回、未公表9回、要確認3回（合計52回）。未調査・未評価・仕様不明・情報不足は0回。表のセル全体が空文字・単独のハイフン（全角・ダッシュ類を含む）・疑問符・N/A・TBDになっている箇所は0件。Markdownの区切り行とMermaidの矢印は空欄として数えていない。

「確認できず」「確認できていない」「確認しにくい」や材質表記の揺れも確認した。同じ不足の表・本文・メーカー一覧での反復は1項目にまとめ、張力と反応、原料の一部と詳細処方など判断が異なる概念は分けた。発売年を一括して未確認としているメーカー概要は、対象製品群を1項目として数え、個々の製品の発売年をすべて調査済みとは扱わない。下表の行番号と「現在の記述」は上記基準SHAのもので、編集後の行番号ではない。

調査項目は **63件**。A=12、B=15、C=19、D=13、E=4。Dには取得不能や旧資料の追加調査が必要な項目を残した。この集計は未指定の文字数や製品数ではない。

- A：一次資料に客観仕様がある。
- B：メーカー説明がある。独立した評価・測定結果ではない。
- C：今回確認した公式資料では未確認。非公開と断定しない。
- D：追加調査が必要。取得失敗も含む。
- E：該当する現行製品・弦種を公式資料で確認できない。不存在や終売の証明ではない。

一般的な試奏・適合の確認を勧める文や、資料全体の読み方は不足製品情報として数えていない。たとえばClarityの音色は要試奏、Melosの手元の弦への適合、未知の症状を選ぶフローチャートはそのまま維持した。松脂の「未公表」についての総論は、個別5製品の確認結果に合わせて確認範囲を示す説明に改めた。

## 調査項目

### Thomastik-Infeld

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:30](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L30) | Thomastik-Infeld / Superflexible（チェロ） | サイズ・ゲージ・物理的張力 | 張力・反応の目安：未指定（本文には4/4・mediumあり） | [superflexible]、[CAT] | A | 4/4・振動弦長70.0 cm・medium。A/D/G/C = 14.8 / 14.5 / 14.3 / 13.6 kg。 | #423：仕様表に補完。ゲージ区分とkg値を区別。 |
| 02 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:30](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L30) | Thomastik-Infeld / Superflexible（チェロ） | 音色 | 未指定 | [RO-F] | B | やや明るく集中的というメーカー説明。チャートは配置を目視確認。 | #423：公式説明または公式音色チャートと明記。実測評価にはしない。 |
| 03 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:30](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L30) | Thomastik-Infeld / Superflexible（チェロ） | 反応速度 | 未指定 | [superflexible]、[superflexible-shop]、[CAT] | C | 今回確認した公式資料では反応速度を確認できず。 | #423：未確認の範囲を説明。張力や制御性から速度を推測しない。 |
| 04 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:30](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L30) | Thomastik-Infeld / Superflexible（チェロ） | 推奨用途 | 未指定 | [superflexible]、[superflexible-shop]、[CAT] | C | 今回確認した公式資料では特定用途の推奨を確認できず。 | #423：確認状況を明示。音色チャートから用途を創作しない。 |
| 05 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:31](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L31) | Thomastik-Infeld / Peter Infeld（チェロ） | サイズ・ゲージ・物理的張力 | 張力・反応の目安：未指定（本文には4/4・mediumあり） | [peter-infeld]、[CAT] | A | 4/4・振動弦長70.0 cm・medium。A/D/G/C = 18.4 / 14.4 / 14.0 / 13.7 kg。 | #423：仕様表に補完。ゲージ区分とkg値を区別。 |
| 06 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:31](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L31) | Thomastik-Infeld / Peter Infeld（チェロ） | 音色 | 未指定 | [PI-F] | B | 中心のある音の芯、力強い中音域、豊かな音色というメーカー説明。チャートは配置を目視確認。 | #423：公式説明または公式音色チャートと明記。実測評価にはしない。 |
| 07 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:31](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L31) | Thomastik-Infeld / Peter Infeld（チェロ） | 反応速度 | 未指定 | [PI-F]、[PI-L] | C | 今回確認した公式資料では反応速度を確認できず。制御のしやすさの訴求は確認。 | #423：未確認の範囲を説明。張力や制御性から速度を推測しない。 |
| 08 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:31](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L31) | Thomastik-Infeld / Peter Infeld（チェロ） | 対象奏者・用途 | 未指定 | [PI-L]、[PI-F] | B | 経験のあるアマチュアからプロまで。メーカーの対象説明。 | #423：公式説明として掲載。独奏・オケ等を推測しない。 |
| 09 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:32](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L32) | Thomastik-Infeld / Dominant Pro（チェロ） | サイズ・ゲージ・物理的張力 | 張力・反応の目安：未指定（本文には4/4・mediumあり） | [dominant-pro]、[CAT] | A | 4/4・振動弦長70.0 cm・medium。A/D/G/C = 18.2 / 14.2 / 13.8 / 13.4 kg。 | #423：仕様表に補完。ゲージ区分とkg値を区別。 |
| 10 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:32](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L32) | Thomastik-Infeld / Dominant Pro（チェロ） | 音色 | 未指定 | [DP-F] | B | 暖かい基調・明るい倍音・音色変化というメーカー説明。チャートは配置を目視確認。 | #423：公式説明または公式音色チャートと明記。実測評価にはしない。 |
| 11 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:32](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L32) | Thomastik-Infeld / Dominant Pro（チェロ） | 反応 | 未指定 | [DP-F] | B | Dominant Proは同社チェロ弦で最も速く直接的、RO41XPはRO41より速いとメーカーが訴求。 | #423：メーカー比較の範囲を示して掲載。 |
| 12 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:32](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L32) | Thomastik-Infeld / Dominant Pro（チェロ） | 対象奏者・用途 | 未指定 | [DP-F] | B | プロ向け。メーカーの対象説明。 | #423：公式説明として掲載。独奏・オケ等を推測しない。 |
| 13 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:33](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L33) | Thomastik-Infeld / Rondo Experience（チェロ） | サイズ・ゲージ・物理的張力 | 張力・反応の目安：未指定（本文には4/4・mediumあり） | [rondo-experience]、[CAT] | A | 4/4・振動弦長70.0 cm・medium。Aのみ18.1 kg。 | #423：仕様表に補完。ゲージ区分とkg値を区別。 |
| 14 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:33](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L33) | Thomastik-Infeld / Rondo Experience（チェロ） | 音色 | 未指定 | [RO-F] | B | 通常のRO41より輝き・倍音が豊かというメーカー説明。チャートは配置を目視確認。 | #423：公式説明または公式音色チャートと明記。実測評価にはしない。 |
| 15 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:33](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L33) | Thomastik-Infeld / Rondo Experience（チェロ） | 反応 | 未指定 | [RO-F] | B | Dominant Proは同社チェロ弦で最も速く直接的、RO41XPはRO41より速いとメーカーが訴求。 | #423：メーカー比較の範囲を示して掲載。 |
| 16 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:33](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L33) | Thomastik-Infeld / Rondo Experience（チェロ） | 対象奏者・用途 | 未指定 | [RO-F] | B | 音の密度が高い楽器や負担軽減が必要な場合。メーカーの対象説明。 | #423：公式説明として掲載。独奏・オケ等を推測しない。 |
| 17 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:34](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L34) | Thomastik-Infeld / Spirit!（チェロ） | サイズ・ゲージ・物理的張力 | 張力・反応の目安：未指定（本文には4/4・mediumあり） | [spirit]、[CAT] | A | 4/4・振動弦長70.0 cm・medium。A/D/G/C = 17.5 / 14.3 / 14.3 / 13.6 kg。 | #423：仕様表に補完。ゲージ区分とkg値を区別。 |
| 18 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:34](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L34) | Thomastik-Infeld / Spirit!（チェロ） | 音色 | 未指定 | [RO-F] | B | 暖かく広がるというメーカー説明。チャートは配置を目視確認。 | #423：公式説明または公式音色チャートと明記。実測評価にはしない。 |
| 19 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:34](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L34) | Thomastik-Infeld / Spirit!（チェロ） | 反応速度 | 未指定 | [spirit]、[spirit-shop]、[CAT] | C | 今回確認した公式資料では反応速度を確認できず。 | #423：未確認の範囲を説明。張力や制御性から速度を推測しない。 |
| 20 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:34](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L34) | Thomastik-Infeld / Spirit!（チェロ） | 推奨用途 | 未指定 | [spirit]、[spirit-shop]、[CAT] | C | 今回確認した公式資料では特定用途の推奨を確認できず。 | #423：確認状況を明示。音色チャートから用途を創作しない。 |
| 21 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:35](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L35) | Thomastik-Infeld / Präzision（チェロ） | サイズ・ゲージ・物理的張力 | 張力・反応の目安：未指定（本文には4/4・mediumあり） | [prazision]、[CAT] | A | 4/4・振動弦長70.0 cm・medium。A/D/G/C = 14.8 / 14.5 / 14.3 / 14.0 kg。 | #423：仕様表に補完。ゲージ区分とkg値を区別。 |
| 22 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:35](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L35) | Thomastik-Infeld / Präzision（チェロ） | 音色 | 未指定 | [RO-F] | B | 集中的というメーカー説明。チャートは配置を目視確認。 | #423：公式説明または公式音色チャートと明記。実測評価にはしない。 |
| 23 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:35](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L35) | Thomastik-Infeld / Präzision（チェロ） | 反応速度 | 未指定 | [prazision]、[prazision-shop]、[CAT] | C | 今回確認した公式資料では反応速度を確認できず。 | #423：未確認の範囲を説明。張力や制御性から速度を推測しない。 |
| 24 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:35](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L35) | Thomastik-Infeld / Präzision（チェロ） | 推奨用途 | 未指定 | [prazision]、[prazision-shop]、[CAT] | C | 今回確認した公式資料では特定用途の推奨を確認できず。 | #423：確認状況を明示。音色チャートから用途を創作しない。 |
| 25 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:33](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L33) | Thomastik-Infeld / Rondo Experience（チェロ） | D/G/C弦の存在・仕様 | D/G/C = 未指定 | [rondo-experience]、[RO-F] | E | チェロ用公式ページでA弦RO41XPのみ確認。Rondo通常セットのD/G/Cとは別扱い。 | #423：A弦のみ確認と記載。D/G/Cの仕様は推測しない。 |
| 26 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L15) | Thomastik-Infeld / Alphayue・Dominant・Spirocore・Belcanto Gold・Versum・Versum Solo・Rondo・Superflexible・Peter Infeld・Dominant Pro・Rondo Experience・Spirit!・Präzision（チェロ） | 発売年の全件確認 | 全シリーズの発売年を確認できていない | [TI]、[CAT]、[PI-F]、[DP-F]、[RO-F] | D | 仕様ページ・カタログ・解説PDFには、全13シリーズについてチェロ用発売年を確定できる一覧がない。PDF名・アップロード日時は発売日ではない。 | 現状維持。シリーズ別の公式発表・旧カタログを追加調査する。 |
| 27 | [docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:26](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md#L26) | Thomastik-Infeld / Belcanto Gold・旧Belcanto（チェロ） | 製品の同一性・名称変更 | Belcantoとの同一性は未確認 | [BG]、[CAT] | C | 現行仕様は確認できるが、単なる名称変更とする根拠は確認できず。 | 現状維持。型番が似ているだけで同一製品にしない。 |

### Jargar

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28 | [docs/strings/manufacturers/strings-manufacturer-jargar.md:28](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-jargar.md#L28) | Jargar / Eccentric（チェロ） | 音色 | 未指定 | [J-H] | B | 暖かい音の芯、豊かな音色、明瞭な輪郭。公式トップのチェロ用製品紹介に説明あり。 | #424：公式説明と明記。比較条件付きの独立評価がないことと区別。 |
| 29 | [docs/strings/manufacturers/strings-manufacturer-jargar.md:28](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-jargar.md#L28) | Jargar / Eccentric（チェロ） | 反応 | Medium（反応は未指定） | [J-H] | B | 速いアーティキュレーション、集中的な反応。公式トップのチェロ用製品紹介に説明あり。 | #424：公式説明と明記。比較条件付きの独立評価がないことと区別。 |
| 30 | [docs/strings/manufacturers/strings-manufacturer-jargar.md:28](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-jargar.md#L28) | Jargar / Eccentric（チェロ） | 推奨用途 | 未指定 | [J-H]、[J-S] | C | 独奏・室内楽・オケ等を指定する公式説明は今回未確認。 | #424：特定用途の推奨は今回確認した公式資料では未確認と記載。 |
| 31 | [docs/strings/manufacturers/strings-manufacturer-jargar.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-jargar.md#L15) | Jargar / Eccentric（チェロ） | 発売時期 | Evoke以外の発売年は未確認 | [J-D] | A | ECCENTRIC CELLOの公開案内にLaunch September 2025と明記。 | #424：2025年9月発売を補完。ヴァイオリン欄とは別に確認。 |
| 32 | [docs/strings/manufacturers/strings-manufacturer-jargar.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-jargar.md#L15) | Jargar / Young Talent・Classic・Superior・Special（チェロ） | 発売年 | Evoke以外の発売年は未確認 | [J-CAT]、[J-HIST]、[J-D] | D | カタログ・沿革・公開キャンペーンで、4シリーズの発売年を一括確定できず。創業年は各製品の発売年と同一ではない。 | 現状維持。シリーズ別の旧公式発表を追加調査する。 |
| 33 | [docs/strings/manufacturers/strings-manufacturer-jargar.md:38](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-jargar.md#L38) | Jargar / Silver Sound（チェロ） | 終売年月 | 終売年月は未指定 | [J-A]、[J-HIST]、[J-CAT] | C | cancel product表記は確認。終売年月は確認できず。2024年カタログ内の資料日付からは確定できない。 | #424：確認範囲を明記し、終売年月は補完しない。 |

### Pirastro

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 34 | [docs/strings/manufacturers/strings-manufacturer-pirastro.md:37](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-pirastro.md#L37) | Pirastro / Gold（チェロ） | 推奨用途 | 未指定 | [P-G]、[P-PDF] | C | 今回確認したチェロ用公式ページ・データシートでは確認できず。価格に対する価値の訴求から用途を推測しない。 | #425：確認状況と資料の範囲を明示。他楽器用GoldやEvah Pirazzi Goldの情報を流用しない。 |
| 35 | [docs/strings/manufacturers/strings-manufacturer-pirastro.md:37](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-pirastro.md#L37) | Pirastro / Gold（チェロ） | 発売年 | 未指定 | [P-G]、[P-PDF]、[P-N] | C | 今回確認したチェロ用公式ページ・データシート・公式ニュースでは確認できず。価格に対する価値の訴求から用途を推測しない。 | #425：確認状況と資料の範囲を明示。他楽器用GoldやEvah Pirazzi Goldの情報を流用しない。 |
| 36 | [docs/strings/manufacturers/strings-manufacturer-pirastro.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-pirastro.md#L15) | Pirastro / Chromcor・Piranito・Obligato・Evah Pirazzi・Evah Pirazzi Gold・Evah Pirazzi Soloist・Perpetual・Permanent・Permanent Soloist・Passione Steel・Passione Gut・Oliv・Eudoxa・Chorda・Flexocor Deluxe・Student Cello Set（チェロ） | 発売年 | 多くのシリーズで未確認。Chromcor・Piranito・Evah Pirazzi・Evah Pirazzi Gold・Evah Pirazzi Soloist・Eudoxa・Flexocor Deluxeの注意欄も同趣旨。 | [P-C]、[P-N] | D | 個別の公式発売告知とチェロ用仕様の照合は全件完了していない。 | 既存の確認できずを維持。シリーズ別に発表・旧公式カタログを追加調査する。 |

### D’Addario

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 37 | [docs/strings/manufacturers/strings-manufacturer-daddario.md:26](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-daddario.md#L26) | D’Addario / Kaplan（チェロ） | 弦別コア・巻線 | steel core（弦別構造は要確認） | [D-K]、[D-IMG] | A | 4/4・弦長700 mmのKS511–KS514。コアA/D=solid steel、G/C=stranded steel。巻線A=titanium、D=nickel、G/C=tungsten。公式画像を目視確認。 | #426：弦別仕様を補完。画像内張力数値は単位明記がないため転記しない。 |
| 38 | [docs/strings/manufacturers/strings-manufacturer-daddario.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-daddario.md#L15) | D’Addario / Prelude・Pro-Arté・Helicore・Kaplan・NS Electric（チェロ） | 発売年 | 全シリーズの発売年を確認できていない | [D-C]、[D-K] | D | 現行一覧・Kaplanの仕様では全5シリーズの発売年は確定できず。 | 現状維持。シリーズ別の公式旧発表・製品資料を追加調査する。 |

### Larsen

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | [docs/strings/manufacturers/strings-manufacturer-larsen.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-larsen.md#L15) | Larsen / Original・Soloist・Magnacore（チェロ） | 発売年 | 既知4製品以外は未確認。Soloistの注意欄も確認できず。 | [L-C]、[L-O]、[L-S]、[L-M]、[L-H] | D | 製品ページと沿革を確認したが、この調査では各シリーズの発売年を確定できず。最初のA弦の開発時期をフルセットの発売年に流用しない。 | 現状維持。単弦・フルセット・ゲージ別の発売告知を追加調査する。 |

### Warchal

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | [docs/strings/manufacturers/strings-manufacturer-warchal.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-warchal.md#L15) | Warchal / Amber（チェロ） | 発売年 | Brilliant以外の発売年は未確認 | [W-A] | C | チェロ用現行製品ページと公式サイト限定検索では発売年を確認できず。 | 現状維持。2013年等の他楽器用Amberの情報は流用しない。 |

### Savarez/Corelli

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41 | [docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md:29](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md#L29) | Savarez/Corelli / Corelli New Concept（チェロ） | 現行製品としての存在 | 現行チェロ用シリーズとして確認できず（メーカー一覧16行目にも同趣旨） | [S-C]、[S-M] | E | 現行カタログのチェロ用はSolea 680M/680Fを確認。対象名称の現行チェロ用製品は確認できず。 | 現状維持。確認できないことを終売と断定せず、Solea等の仕様も流用しない。 |
| 42 | [docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md#L15) | Savarez/Corelli / Corelli New Concept（チェロ） | 過去仕様・販売時期・終売時期 | 未確認（29行目にも同趣旨） | [S-C]、[S-M] | D | 現行カタログは過去の仕様・期間を立証しない。旧メーカー資料は今回特定できず。 | 現状維持。旧公式カタログ・アーカイブを追加調査。販売店の名称だけで補完しない。 |
| 43 | [docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md:29](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md#L29) | Savarez/Corelli / Corelli Gut（チェロ） | 現行製品としての存在 | 現行チェロ用シリーズとして確認できず（メーカー一覧16行目にも同趣旨） | [S-C]、[S-M] | E | 現行カタログのチェロ用はSolea 680M/680Fを確認。対象名称の現行チェロ用製品は確認できず。 | 現状維持。確認できないことを終売と断定せず、Solea等の仕様も流用しない。 |
| 44 | [docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md#L15) | Savarez/Corelli / Corelli Gut（チェロ） | 過去仕様・販売時期・終売時期 | 未確認（29行目にも同趣旨） | [S-C]、[S-M] | D | 現行カタログは過去の仕様・期間を立証しない。旧メーカー資料は今回特定できず。 | 現状維持。旧公式カタログ・アーカイブを追加調査。販売店の名称だけで補完しない。 |

### 松脂

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45 | [docs/rosin/major-rosins.md:76](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L76) | Pirastro Cellisto（チェロ向け） | 詳細配合・原料比率 | 詳細配合／詳細処方は未公表 | [P-R] | C | 詳細な原料比率・全処方は今回確認した公式資料では未確認。一般的な製法を秘密とする公式説明はあるが、個別製品の全成分まで確認できるわけではない。 | #427：未公表の断定を避けて確認範囲を記載。 |
| 46 | [docs/rosin/major-rosins.md:77](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L77) | Pirastro Cello（チェロ向け） | 詳細配合・原料比率 | 詳細配合／詳細処方は未公表 | [P-R] | C | 詳細な原料比率・全処方は今回確認した公式資料では未確認。一般的な製法を秘密とする公式説明はあるが、個別製品の全成分まで確認できるわけではない。 | #427：未公表の断定を避けて確認範囲を記載。 |
| 47 | [docs/rosin/major-rosins.md:79](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L79) | Kolstein Supreme Cello（チェロ向け） | 詳細配合・原料比率 | 詳細配合／詳細処方は未公表 | [K-R]、[K-H]、[K-SDS] | D | 詳細な原料比率・全処方は今回確認した公式資料では未確認。製品・解説ページを確認。公式MSDSリンクは404で本文を取得できず。 | #427：未公表の断定を避けて確認範囲を記載。MSDSの有効な公式配布先は追加調査。 |
| 48 | [docs/rosin/major-rosins.md:98](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L98) | D’Addario Clarity Hypoallergenic（チェロ向け） | 詳細配合・原料比率 | 詳細配合／詳細処方は未公表 | [D-R] | C | 詳細な原料比率・全処方は今回確認した公式資料では未確認。 | #427：未公表の断定を避けて確認範囲を記載。 |
| 49 | [docs/rosin/major-rosins.md:109](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L109) | Leatherwood Bespoke（チェロ向け） | 詳細配合・原料比率 | 詳細配合／詳細処方は未公表 | [LW] | C | 詳細な原料比率・全処方は今回確認した公式資料では未確認。 | #427：未公表の断定を避けて確認範囲を記載。 |
| 50 | [docs/rosin/major-rosins.md:98](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L98) | D’Addario / Clarity（violin・viola・cello） | 確認できる主原料 | 低アレルギー訴求ライン。配合詳細は未公表。 | [D-R] | A | 公式にsynthetic hydrocarbon resinと明記。 | #427：合成炭化水素樹脂を補完。詳細添加物や低アレルギーの効用とは区別。 |
| 51 | [docs/rosin/major-rosins.md:109](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L109) | Leatherwood / Bespoke（チェロ） | 原料・レシピの選択肢 | カスタム思想。詳細処方は未公表。 | [LW] | A | オーストラリア産松樹脂、チェロ用Supple/Crispと個別ブレンドを確認。 | #427：確認できる原料と楽器別レシピを補完。原料の詳細比率は推測しない。 |
| 52 | [docs/rosin/major-rosins.md:83](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L83) | Melos / Cello Baroque（Cello & Bass Viol） | 設計対象 | Baroque用途名義の派生系。通常運用に加える前に用途適合を要確認。 | [M-B] | B | 公式は特にガット弦向けに設計と説明。 | #427：公式の設計対象を追記。自分の弦との用途適合を確認する助言は維持。 |
| 53 | [docs/rosin/major-rosins.md:88](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L88) | W.E. Hill & Sons / Premium Cello（チェロ） | 正式名称・型番・仕様の一次情報 | Premium Dark Cello名義は販売情報で確認。代理店/販売店記載差異を要確認。 | [H-R] | A | Hidersine公式で2067M、Cello、Dark/Medium、主成分colophony/natural oilsを確認。 | #427：公式資料の名称・型番に整理。通常のHill Dark 2064と区別。 |
| 54 | [docs/rosin/major-rosins.md:118](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L118) | CECILIA / Artist Reserve Prima・Divinum（cello/viola） | チェロ向け販売開始・在庫 | 2026年10月予定。販売開始・在庫状況は未確認。 | [CE] | C | 現行の公式ページもLaunching October 2026と予定を掲載。チェロ向け販売開始日・在庫の確証なし。 | 現状維持。発売予定を販売開始済みとは扱わない。 |
| 55 | [docs/rosin/major-rosins.md:78](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L78) | Pirastro / Oliv・Evah Pirazzi Rosin（ガット弦・Evah Pirazzi弦向け） | 対応弦・製品特性 | 製品ライン名は公式掲載。チェロ専用表記は要追加確認。 | [P-R] | B | 比較的柔らかい、低粉塵、ガット弦・Evah Pirazzi弦向けという公式説明。 | #427：確認できる説明を掲載。独立した低粉塵比較とは扱わない。 |
| 56 | [docs/rosin/major-rosins.md:78](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L78) | Pirastro / Oliv・Evah Pirazzi Rosin（チェロ専用か） | チェロ専用表記 | チェロ専用表記は要追加確認。 | [P-R] | C | 対応する弦の種類は確認できるが、チェロ専用とする記載は今回未確認。 | #427：確認範囲を明示。対応弦から専用品とは推測しない。 |
| 57 | [docs/rosin/major-rosins.md:85](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L85) | Petz / Soloist（チェロ用の有無） | チェロ向け製品・仕様 | Soloist名称は流通で確認、チェロ専用かは要追加確認。 | [PZ]、[PZ-S] | E | 現行公式製品紹介ではviolin/viola向けsoft/hardのみ確認。旧公式ショップ一覧は検索でcello表記も出るが直接取得できず。 | #427：確認できたVn/Va用掲載を記載。チェロ用の不存在とは断定しない。 |
| 58 | [docs/rosin/major-rosins.md:86](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L86) | Petz / Vienna’s Best（チェロ用・violin/viola用） | チェロ用の一次情報 | 汎用系・販売店情報ベース、流通記載中心。 | [PZ] | A | メーカー公式製品紹介はチェロ用とviolin/viola用を別掲載。 | #427：チェロ向けあり・公式情報ありへ補完。 |
| 59 | [docs/rosin/major-rosins.md:87](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/rosin/major-rosins.md#L87) | Nyman / Cello（チェロ） | メーカー一次仕様 | Cello表記で流通。公式仕様詳細は要追加確認。 | メーカー公式URL未特定 | D | 検索では販売店情報にとどまり、メーカーの公式URLと仕様書を特定できず。 | 販売店情報ベースを維持。#427でメーカー一次資料が未特定であることを補足。 |

### 駒

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 | [docs/bridges/bridges-blank-manufacturers.md:15](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/bridges/bridges-blank-manufacturers.md#L15) | Milo Stamm Ponticelli（チェロ駒） | 本拠地 | 本拠地未確認 | [MS-C]、[MS-T] | D | 公式ページの直接取得はタイムアウト・503。検索で規約の返送先Indjija/Serbienは再確認したが、住所だけでは本拠地・製造国の立証にならない。 | 現状維持。公式企業紹介・製造説明を再取得して確認する。 |
| 61 | [docs/bridges/bridges-blank-manufacturers.md:18](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/bridges/bridges-blank-manufacturers.md#L18) | Milo Stamm Ponticelli（チェロ駒） | 製造国 | 公式チェロ駒ページと規約に明示がないため未指定（81行目も同趣旨） | [MS-C]、[MS-T] | D | 公式ページの直接取得はタイムアウト・503。検索で規約の返送先Indjija/Serbienは再確認したが、住所だけでは本拠地・製造国の立証にならない。 | 現状維持。公式企業紹介・製造説明を再取得して確認する。 |

### 弓

| ID | ファイル・基準行 | メーカー・製品・対象楽器 | 不足項目 | 現在の記述 | 一次資料 | 分類 | 結果・判断理由 | 修正・保留理由 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 62 | [docs/bows/manufacturers.md:42](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/bows/manufacturers.md#L42) | Ary France（チェロを含む弓） | 設立年・沿革 | メーカー公式の一次情報を一元的に確認しにくいため断定しません | [ARY] | D | メーカー公式URLを特定できず、旧公式サイト候補も取得不可。別業種のARY Franceのカタログは根拠にしない。 | 現状維持。正当なメーカー公式資料を特定するまで販売店の沿革を転記しない。 |
| 63 | [docs/bows/manufacturers.md:78](https://github.com/arscombinatoria/cello-parts-log/blob/e58e9a2c931bd79b461c2335d1dad2cb9fb93c48/docs/bows/manufacturers.md#L78) | Yamaha / CBB-301（チェロ弓） | 地域による材質表記の差 | Carbon Fiber / CFRP / GFRPなど揺れがあるためカーボン系として扱う | [Y-S] | D | 参照先の米国公式仕様は403で取得不可。地域・型番の対応を今回再検証できず。 | 現状維持。各地域の同型番・仕様版を照合するまで単一素材と断定しない。 |

## 補完値と制限

Thomastik-Infeldの4/4・振動弦長70.0 cm・mediumの張力は次のとおり。kgは公式の表記を維持し、ゲージ区分・押弦感・反応速度とは区別した。

| 製品 | A kg | D kg | G kg | C kg |
| --- | --- | --- | --- | --- |
| Superflexible | 14.8 | 14.5 | 14.3 | 13.6 |
| Peter Infeld | 18.4 | 14.4 | 14.0 | 13.7 |
| Dominant Pro | 18.2 | 14.2 | 13.8 | 13.4 |
| Rondo Experience | 18.1 | A弦のみ確認 | A弦のみ確認 | A弦のみ確認 |
| Spirit! | 17.5 | 14.3 | 14.3 | 13.6 |
| Präzision | 14.8 | 14.5 | 14.3 | 14.0 |

Peter Infeldのフライヤーのテキスト抽出にはRO型番が重複して混入するため、PI41–PI44の値は製品ページと現行カタログ112ページで照合した。現行カタログPDFは画像主体で、110・112・114・116・118・124ページをOCRでも確認した。RO41XPは独立したA弦として扱い、Rondo通常セットのD/G/CをRondo Experienceの仕様にはしない。

追加の選定情報として、同じ松脂セル内にPirastro Celloのやや硬め／Cellistoの柔らかいという公式説明、KolsteinのNormal/Mediumの2種を補った。これら3件は詳細処方とは別の補足情報で、上の不足項目数には加算していない。

音色チャートは定性的なメーカーの配置を要約した。反応・音色の説明はメーカーの訴求であり、共通条件での独立した測定・比較試奏を本調査で行ったものではない。発売年・終売年月はPDF名や作成年、サイト掲載日から推定していない。

## PRの分割と変更ファイル

| PR | 単位 | 変更ファイル |
| --- | --- | --- |
| [#423](https://github.com/arscombinatoria/cello-parts-log/pull/423) | Thomastik-Infeldの仕様・公式説明 | `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md` |
| [#424](https://github.com/arscombinatoria/cello-parts-log/pull/424) | Jargar EccentricとSilver Soundの確認範囲 | `docs/strings/manufacturers/strings-manufacturer-jargar.md` |
| [#425](https://github.com/arscombinatoria/cello-parts-log/pull/425) | Pirastro Goldの確認範囲 | `docs/strings/manufacturers/strings-manufacturer-pirastro.md` |
| [#426](https://github.com/arscombinatoria/cello-parts-log/pull/426) | D’Addario Kaplanの弦別構造 | `docs/strings/manufacturers/strings-manufacturer-daddario.md` |
| [#427](https://github.com/arscombinatoria/cello-parts-log/pull/427) | 松脂の原料・仕様・公式説明と処方の確認範囲 | `docs/rosin/major-rosins.md` |
| 本調査記録のPR | 全体棚卸し・分類・次の調査への引継ぎ | `research/2026-10-24-product-information-audit.md` |

全修正PRは調査開始時の同じmainのSHAから分岐し、他の修正PRのコミットを含めない。提出中にmainへ入った依存関係更新2件は、履歴を書き換えず各ブランチへマージして再検証する。調査開始時の未マージPR #410 / #395はGitHubの変更ファイル一覧でpackage.json・package-lock.jsonのみと確認し、対象文書の重複はなかった。新規PRは独立したファイルを変更する。既存PRは書き換えず、マージもしない。

今後のPRは、Dの裏付けが得られたものから次の単位に分ける。

1. Thomastik-Infeldのチェロ用発売史。単弦／セット／他楽器用の発表を区別する。
2. Jargarの旧チェロ製品の発売史。EccentricとEvokeの確認済み年月は維持する。
3. Pirastroのチェロ用発売史。Goldの裏付けのない年月は追加しない。
4. D’Addarioのチェロ用発売史。Kaplanの構造修正と分離する。
5. LarsenのOriginal／Soloist／Magnacoreの発売史。弦種別の公開時期を区別する。
6. Savarez/Corelliの旧名称を立証する旧公式資料。製品の存在確認から行う。
7. Milo Stammの企業所在地・製造情報。返送先だけでは補完しない。
8. 弓はAry Franceの一次資料特定とYamaha CBB-301の地域仕様照合を別PRにする。
9. Kolsteinの有効な公式SDS取得。安全データシートに全処方がない場合も、非公開の断定には使わない。

C/Eの項目は、新たな公式資料が確認できた時点で再調査する。空欄をなくす目的だけの追加修正は勧めない。

## 検証・同期

各サイト文書の変更を独立したブランチで `npm run lint`、`npm test`、`npm run build`、`git diff --check` により検証した。`npm test` は型チェックであり、比較試験や単体テストではない。表の列数・Markdown構文・追加参考リンクの出典内容・既存内部リンクも点検した。

最初の型チェックは環境の古いnode_modulesにTypeScriptがなく失敗した。最新mainのロックファイルに対して `npm ci` を実行し、以後の検証は成功した。ビルドには既存のblogディレクトリ不在とDocusaurusの更新確認権限の警告があるが、MDX処理と静的ファイル生成は成功した。外部リンクはビルドのみでは検証されないため、資料の閲覧・取得状況を出典欄にも記録している。

各PRの提出前に `git fetch origin main` を行った。#423〜#426の初回提出時は `e58e9a2c931bd79b461c2335d1dad2cb9fb93c48`。#427の提出直前には依存関係更新 #421 / #422 を含む `b854a9ee69a919cf3c434907d3bc960bb34ad041` に進んでいた。差分はpackage-lock.jsonのみで、docs・AGENTS.md・執筆スキルは不変と確認した。この最新mainを全修正ブランチへ安全にマージし、更新後の `npm ci` と4検証を再実行した。棚卸しの基準SHAと行番号は、文書内容が同一であるため当初のSHAを維持した。GitHubの未マージPRは対象ファイル一覧で重複を確認し、既存の変更を置き換えていない。

## 出典URLと確認範囲

以下は今回閲覧・取得を試みた一次資料のURL。取得に失敗したものは明記した。メーカー公式資料であると特定できない旧サイト候補も、その旨を記載して区別した。

- **TI**: [Thomastik-Infeld チェロ一覧](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello)
- **CAT**: [Thomastik-Infeld 現行公式カタログ](https://www.thomastik-infeld.com/pageflips/catalog/)
- **PI-F**: [Peter Infeld チェロ用フライヤー](https://www.thomastik-infeld.com/pdf/240926_PI_WebFlyer_Cello_EN.pdf)
- **PI-L**: [Peter Infeld シリーズ説明](https://www.thomastik-infeld.com/en/new-releases/peter-infeld/string-line)
- **DP-F**: [Dominant Pro チェロ用解説](https://www.thomastik-infeld.com/pdf/Thomastik-Infeld_DP400_webPDF_EN_LQ.pdf)
- **RO-F**: [Rondo / RO41XP チェロ用解説・音色チャート](https://www.thomastik-infeld.com/database/2022042717092720406.pdf)
- **BG**: [Belcanto Gold チェロ用製品ページ](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/belcanto-gold)
- **J-H**: [Jargar 公式トップの製品紹介](https://jargar-strings.com/)
- **J-S**: [Jargar Eccentric 公式ショップ](https://shop.thomastik-infeld.com/category/orchestral/cello/jargar-eccentric-violoncello/)
- **J-D**: [Jargar 公開キャンペーン案内](https://jargar-strings.com/dealer-area/)
- **J-A**: [Jargar 製品アーカイブ](https://jargar-strings.com/category/all/)
- **J-HIST**: [Jargar 公式沿革](https://jargar-strings.com/the-history/)
- **J-CAT**: [Jargar 2024年公式カタログ](https://jargar-strings.com/wp-content/uploads/2024/06/JS-BtC-katalog_04a.pdf)
- **P-G**: [Pirastro Gold チェロ用製品ページ](https://www.pirastro.com/public_pirastro/pages/en/Gold-00004/)
- **P-PDF**: [Pirastro Gold チェロ用データシート](https://www.pirastro.com/public_pirastro/pdf?instrument=285_Cello&locale=en&quality=040_Gold)
- **P-N**: [Pirastro 公式ニュース](https://www.pirastro.com/public_pirastro/pages/en/News/)
- **P-C**: [Pirastro チェロ用一覧](https://www.pirastro.com/public_pirastro/pages/en/Stringfinder-00002/?instrument=285_Cello)
- **D-K**: [Kaplan 公式製品ページ](https://www.daddario.com/products/kaplan-cello-string-set-44-scale-medium-tension)
- **D-IMG**: [Kaplan 公式張力表画像](https://www.daddario.com/cdn/shop/files/learn_more_tension_chart_kaplan_cello_strings.png)
- **D-C**: [D’Addario チェロ弦一覧](https://www.daddario.com/collections/cello-strings)
- **L-C**: [Larsen チェロ用一覧](https://larsenstrings.com/larsen-strings-cello/)
- **L-O**: [Larsen Original](https://larsenstrings.com/original-cello/)
- **L-S**: [Larsen Soloist](https://larsenstrings.com/larsen-soloist/)
- **L-M**: [Larsen Magnacore](https://larsenstrings.com/larsen-magnacore/)
- **L-H**: [Larsen 沿革](https://larsenstrings.com/our-story/)
- **W-A**: [Warchal Amber チェロ用](https://warchal.com/product/amber-cello/)
- **S-C**: [Savarez 現行カタログ](https://www.savarez.com/products-catalog)
- **S-M**: [Corelli Solea 680M](https://www.savarez.com/violoncellesoleacorelli-solea-680m)
- **P-R**: [Pirastro 公式松脂説明](https://www.pirastro.com/public_pirastro/pages/en/Rosin/)
- **K-R**: [Kolstein Supreme Cello 公式製品ページ](https://kolstein.com/products/kolsteins%E2%84%A2-supreme-cello-rosin)
- **K-H**: [Kolstein 公式松脂解説](https://kolstein.com/pages/kolsteins-rosin)
- **K-SDS**: [Kolstein 製品ページからのMSDSリンク（404）](https://kolstein.com/wp-content/uploads/2019/11/Kolstein-Rosin-Products-US-EN-2-sds.pdf)
- **M-B**: [Melos Cello Baroque 公式製品ページ](https://melosrosin.gr/product/melos-rosin-cello-baroque/)
- **H-R**: [Hidersine 公式 Hill Premium Cello](https://www.hidersine.com/w-e-hill-sons/product/289-w-e-hill-premium-cello-rosin)
- **D-R**: [D’Addario Clarity 公式製品ページ](https://www.daddario.com/products/clarity-hypoallergenic-rosin)
- **LW**: [Leatherwood 公式FAQ](https://www.leatherwoodrosin.com.au/pages/faq)
- **CE**: [CECILIA Artist Reserve 公式告知](https://www.ceciliarosincollection.com/artist-reserve/)
- **MS-C**: [Milo Stamm 公式チェロ駒ページ（取得失敗）](https://www.milostamm.com/violoncello.htm)
- **MS-T**: [Milo Stamm 公式規約（検索では返送先を再確認、直接取得失敗）](https://milostamm.com/e_agb.htm)
- **PZ**: [PetzVienna 公式製品紹介](https://pk.at/en_GB/kolophonium)
- **PZ-S**: [Petz旧公式ショップSoloist一覧（取得失敗）](https://www.petzkolophonium.com/shop/lng/en/accessories/kolophonium/petz-kolophonium-vienna/soloist-quality/)
- **ARY**: [旧公式サイトの候補（取得不可・現行公式URLは特定できず）](https://www.ary-fr.com/)
- **Y-S**: [Yamaha 米国公式仕様ページ（403）](https://usa.yamaha.com/products/musical_instruments/strings/bows/cbb301/specs.html)
- **superflexible**: [Superflexible チェロ用公式仕様](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/superflexible)
- **superflexible-shop**: [Superflexible 公式ショップ](https://shop.thomastik-infeld.com/category/orchestral/cello/superflexible-violoncello/)
- **peter-infeld**: [Peter Infeld チェロ用公式仕様](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/peter-infeld)
- **dominant-pro**: [Dominant Pro チェロ用公式仕様](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/dominant-pro)
- **rondo-experience**: [Rondo Experience チェロ用公式仕様](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/rondo-experience)
- **spirit**: [Spirit! チェロ用公式仕様](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/spirit)
- **spirit-shop**: [Spirit! 公式ショップ](https://shop.thomastik-infeld.com/category/orchestral/cello/spirit-violoncello/)
- **prazision**: [Präzision チェロ用公式仕様](https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/prazision)
- **prazision-shop**: [Präzision 公式ショップ](https://shop.thomastik-infeld.com/category/orchestral/cello/prazision-violoncello/)

[TI]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello
[CAT]: https://www.thomastik-infeld.com/pageflips/catalog/
[PI-F]: https://www.thomastik-infeld.com/pdf/240926_PI_WebFlyer_Cello_EN.pdf
[PI-L]: https://www.thomastik-infeld.com/en/new-releases/peter-infeld/string-line
[DP-F]: https://www.thomastik-infeld.com/pdf/Thomastik-Infeld_DP400_webPDF_EN_LQ.pdf
[RO-F]: https://www.thomastik-infeld.com/database/2022042717092720406.pdf
[BG]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/belcanto-gold
[J-H]: https://jargar-strings.com/
[J-S]: https://shop.thomastik-infeld.com/category/orchestral/cello/jargar-eccentric-violoncello/
[J-D]: https://jargar-strings.com/dealer-area/
[J-A]: https://jargar-strings.com/category/all/
[J-HIST]: https://jargar-strings.com/the-history/
[J-CAT]: https://jargar-strings.com/wp-content/uploads/2024/06/JS-BtC-katalog_04a.pdf
[P-G]: https://www.pirastro.com/public_pirastro/pages/en/Gold-00004/
[P-PDF]: https://www.pirastro.com/public_pirastro/pdf?instrument=285_Cello&locale=en&quality=040_Gold
[P-N]: https://www.pirastro.com/public_pirastro/pages/en/News/
[P-C]: https://www.pirastro.com/public_pirastro/pages/en/Stringfinder-00002/?instrument=285_Cello
[D-K]: https://www.daddario.com/products/kaplan-cello-string-set-44-scale-medium-tension
[D-IMG]: https://www.daddario.com/cdn/shop/files/learn_more_tension_chart_kaplan_cello_strings.png
[D-C]: https://www.daddario.com/collections/cello-strings
[L-C]: https://larsenstrings.com/larsen-strings-cello/
[L-O]: https://larsenstrings.com/original-cello/
[L-S]: https://larsenstrings.com/larsen-soloist/
[L-M]: https://larsenstrings.com/larsen-magnacore/
[L-H]: https://larsenstrings.com/our-story/
[W-A]: https://warchal.com/product/amber-cello/
[S-C]: https://www.savarez.com/products-catalog
[S-M]: https://www.savarez.com/violoncellesoleacorelli-solea-680m
[P-R]: https://www.pirastro.com/public_pirastro/pages/en/Rosin/
[K-R]: https://kolstein.com/products/kolsteins%E2%84%A2-supreme-cello-rosin
[K-H]: https://kolstein.com/pages/kolsteins-rosin
[K-SDS]: https://kolstein.com/wp-content/uploads/2019/11/Kolstein-Rosin-Products-US-EN-2-sds.pdf
[M-B]: https://melosrosin.gr/product/melos-rosin-cello-baroque/
[H-R]: https://www.hidersine.com/w-e-hill-sons/product/289-w-e-hill-premium-cello-rosin
[D-R]: https://www.daddario.com/products/clarity-hypoallergenic-rosin
[LW]: https://www.leatherwoodrosin.com.au/pages/faq
[CE]: https://www.ceciliarosincollection.com/artist-reserve/
[MS-C]: https://www.milostamm.com/violoncello.htm
[MS-T]: https://milostamm.com/e_agb.htm
[PZ]: https://pk.at/en_GB/kolophonium
[PZ-S]: https://www.petzkolophonium.com/shop/lng/en/accessories/kolophonium/petz-kolophonium-vienna/soloist-quality/
[ARY]: https://www.ary-fr.com/
[Y-S]: https://usa.yamaha.com/products/musical_instruments/strings/bows/cbb301/specs.html
[superflexible]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/superflexible
[superflexible-shop]: https://shop.thomastik-infeld.com/category/orchestral/cello/superflexible-violoncello/
[peter-infeld]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/peter-infeld
[dominant-pro]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/dominant-pro
[rondo-experience]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/rondo-experience
[spirit]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/spirit
[spirit-shop]: https://shop.thomastik-infeld.com/category/orchestral/cello/spirit-violoncello/
[prazision]: https://www.thomastik-infeld.com/en/products/orchestral-strings/cello/prazision
[prazision-shop]: https://shop.thomastik-infeld.com/category/orchestral/cello/prazision-violoncello/

## 検索で見つかった元の記述（重複を含む）

指定語に加え確認できず・要追加確認等を含めた検索の50行を保存する。1行に複数概念や同じ不足の反復があるため、上の調査項目数とは一致しない。材質表記の揺れは本文の周辺確認で追加した。

- `docs/bows/manufacturers.md:42` — 一方で、メーカー公式の一次情報を一元的に確認しにくいため、設立年や沿革はこのページでは断定しません。
- `docs/bridges/bridges-blank-manufacturers.md:15` —  /  Milo Stamm Ponticelli（ミロ・スタム）  /  本拠地未確認（公式規約の返送先：セルビア・Indjija）※  /  Student / Standard / Premium / Royal（公式の4品質クラス）  /  B / B1 / D / F / F1 / H / H1 / H2 / K / M など（公式掲載の形状モデル。品質クラスとは別軸）  /  ラインが複数あり、予算に応じて段階選択しやすい。取扱店の型番・在庫が比較的多く、同じ工房でグレードを比較しやすい。  / 
- `docs/bridges/bridges-blank-manufacturers.md:18` — ※ Milo Stamm の表に記載した住所は、[公式利用規約](https://www.milostamm.com/e_agb.htm)に返送先として掲載された住所です。この住所は、本拠地やすべての製品の製造地を示すものではありません。[公式チェロ駒ページ](https://www.milostamm.com/violoncello.htm)と同規約では製造国が明示されていないため、製造国は「未指定」とします。
- `docs/bridges/bridges-blank-manufacturers.md:81` — - 公式利用規約には、返送先住所として Zmaj Jovina 185a, 22320 Indjija, Serbien が掲載されています。この住所は、本拠地やすべての製品の製造地を示すものではありません。公式チェロ駒ページと同規約では製造国が明示されていないため、製造国は「未指定」とします。
- `docs/rosin/major-rosins.md:14` — また、配合や製法は企業秘密である場合が多く、公開情報は限定的です。未公表事項は未公表と明示し、販売店情報と公式情報を分けて扱います。
- `docs/rosin/major-rosins.md:27` — - ただし、**具体的な配合比・添加素材の詳細は未公表**である製品が多数です。  
- `docs/rosin/major-rosins.md:70` — > 注記: 「公式情報」はメーカー側の明示事項、「販売店情報ベース」は販売ページ中心の情報です。配合詳細は未公表が多いため、断定的な音質表現は避けています。
- `docs/rosin/major-rosins.md:76` —  /  Pirastro Cellisto  /  チェロ向け  /  公式情報あり  /  Pirastro のチェロ用ライン。詳細配合は未公表。  /  Pirastro Cello との比較で硬さ方向を確認しやすい。  / 
- `docs/rosin/major-rosins.md:77` —  /  Pirastro Cello  /  チェロ向け  /  公式情報あり  /  同社チェロ用の基準候補。詳細配合は未公表。  /  基準銘柄として他製品比較に使いやすい。  / 
- `docs/rosin/major-rosins.md:78` —  /  Pirastro Oliv / Evah Pirazzi Rosin  /  汎用〜チェロ使用例あり  /  公式情報あり  /  製品ライン名は公式掲載。チェロ専用表記は要追加確認。  /  低粉塵・反応の比較対象として運用可能だが用途確認が必要。  / 
- `docs/rosin/major-rosins.md:79` —  /  Kolstein Supreme Cello  /  チェロ向け  /  公式情報あり  /  チェロ用として展開。配合詳細は未公表。  /  専用品群の比較軸に入れやすい。  / 
- `docs/rosin/major-rosins.md:83` —  /  Melos Cello Baroque  /  チェロ向け（用途限定）  /  公式情報あり  /  Baroque 用途名義の派生系。  /  通常運用に加える前に用途適合を要確認。  / 
- `docs/rosin/major-rosins.md:85` —  /  Petz Soloist  /  チェロ使用例あり  /  販売店情報ベース  /  Soloist 名称は流通で確認、チェロ専用かは要追加確認。  /  比較候補にはなるが用途断定は避ける。  / 
- `docs/rosin/major-rosins.md:87` —  /  Nyman Cello  /  チェロ向け  /  販売店情報ベース  /  Cello 表記で流通。公式仕様詳細は要追加確認。  /  実売実績は多いが最新仕様の一次確認を推奨。  / 
- `docs/rosin/major-rosins.md:88` —  /  Hill Premium Dark Cello  /  チェロ向け  /  販売店情報ベース  /  Premium Dark Cello 名義は販売情報で確認。  /  代理店/販売店記載差異を要確認。  / 
- `docs/rosin/major-rosins.md:98` —  /  D’Addario Clarity Hypoallergenic  /  代替系（低アレルギー訴求）  /  公式情報あり  /  低アレルギー訴求ライン。配合詳細は未公表。  /  皮膚刺激懸念時の候補。音色方向は要試奏確認。  / 
- `docs/rosin/major-rosins.md:109` —  /  Leatherwood Bespoke  /  高級・調整系  /  公式情報あり  /  カスタム思想。詳細処方は未公表。  /  基準松脂確定後に導入すると比較しやすい。  / 
- `docs/rosin/major-rosins.md:118` — CECILIA Artist Reserve（Prima / Divinum）は、[公式ページ](https://www.ceciliarosincollection.com/artist-reserve/)で2026年10月発売予定と告知され、両フォーミュラにviolin/viola・cello/viola向けを掲げています。ただし、確認時点（2026年10月24日）ではチェロ向けの販売開始・在庫状況を確認できていないため、現行製品表への追加は保留します。
- `docs/strings/manufacturers/index.md:16` —  /  Savarez/Corelli  /  Corelli Solea（New Concept / Corelli Gut は現行未確認）  /  公式カタログで Solea の掲載を確認  /  スチール系セットの比較  /  中〜中高  /  [詳細ページ](./strings-manufacturer-savarez-corelli.md)  / 
- `docs/strings/manufacturers/strings-manufacturer-daddario.md:15` — - 確認した一次資料では、全シリーズの発売年を確認できていない
- `docs/strings/manufacturers/strings-manufacturer-daddario.md:26` —  /  Kaplan  /  上級〜プロ  /  steel core（弦別構造は要確認）  /  豊かで複雑な音色を目指す設計  /  強い弓圧でも破綻しにくい設計  /  ソロ、出力重視  /  楽器側が硬い場合は張力感の確認推奨  / 
- `docs/strings/manufacturers/strings-manufacturer-jargar.md:15` — - 発売年は Evoke（2023年11月発売）以外、今回確認できた一次資料では未確認
- `docs/strings/manufacturers/strings-manufacturer-jargar.md:28` —  /  Eccentric  /  現行製品  /  A/D = carbon steel core + multialloy 巻線、G/C = spiralcore + tungsten/nickel 巻線  /  未指定  /  Medium（反応は未指定）  /  未指定  /  4/4、A/D/G/C 単弦・セット  / 
- `docs/strings/manufacturers/strings-manufacturer-jargar.md:36` — 現行シリーズと Eccentric の仕様は、2026年10月24日に公式チェロ一覧と公式製品ページで確認しました。Eccentric の音色・反応・推奨用途は、比較条件を伴う評価を確認できていないため未指定としています。
- `docs/strings/manufacturers/strings-manufacturer-jargar.md:38` — Silver Sound は、公式の[製品アーカイブ](https://jargar-strings.com/category/all/)で「Silver Sound Violoncello cancel product」として掲載されているため、終売扱いとして現行シリーズ一覧から除外しています。終売年月は未指定です。
- `docs/strings/manufacturers/strings-manufacturer-larsen.md:15` — - 発表・発売時期は Sovereign（2026年4月24日発表、公式告知では2026年5月から世界展開）、Aurora（2021年公開）、Il Cannone（2020年リリース）、Magnacore Arioso（2017年フルセット完成）以外は今回確認できた一次資料では未確認
- `docs/strings/manufacturers/strings-manufacturer-larsen.md:27` —  /  Soloist  /  出力重視  /  Original 系のソロ志向設定  /  前に出る音像を狙う方向  /  押弦感は強めになりやすい  /  独奏  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:15` — - 発売年は、今回確認できた一次資料では多くのシリーズで未確認
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:23` —  /  Chromcor  /  入門〜実用  /  steel strings  /  明瞭で扱いやすい方向  /  反応が速い  /  学習、日常運用  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:24` —  /  Piranito  /  入門  /  steel strings  /  素直で輪郭を出しやすい方向  /  安定志向  /  初学者、学校用途  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:26` —  /  Evah Pirazzi  /  上位  /  チェロ用は steel strings  /  密度と出力を狙う方向  /  速い反応  /  ソロ、投射重視  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:27` —  /  Evah Pirazzi Gold  /  上位派生  /  チェロ用は steel strings  /  滑らかさを加えた方向  /  反応としなやかさの両立志向  /  上位音色調整  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:28` —  /  Evah Pirazzi Soloist  /  上位派生  /  steel strings 系列  /  前方投射を狙う方向  /  張力感は強めになりやすい  /  独奏  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:35` —  /  Eudoxa  /  伝統系  /  gut strings  /  柔らかい質感を狙う方向  /  反応は穏やか寄り  /  伝統系運用  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:37` —  /  Gold  /  現行ガット弦  /  羊ガットコア、A/D = アルミ巻、G/C = 銀巻  /  明るいガットの音色（公式説明）  /  4/4・medium の張力：A 13.6 / D 12.0 / G 12.0 / C 12.2 kg。速い反応（公式説明）  /  未指定  /  発売年：未指定。[チェロ用公式仕様](https://www.pirastro.com/public_pirastro/pages/en/Gold-00004/)を参照  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:38` —  /  Flexocor Deluxe  /  実用上位  /  steel strings  /  まとまりと明瞭さの両立志向  /  安定感重視  /  オケ、アンサンブル  /  発売年は今回確認できず  / 
- `docs/strings/manufacturers/strings-manufacturer-pirastro.md:55` — Gold は Passione (Gut)、Oliv、Eudoxa、Chorda とともに[公式のチェロ用 Gut Strings 一覧](https://www.pirastro.com/public_pirastro/pages/en/Stringfinder-00002/?instrument=285_Cello&material=D)に掲載される現行製品です。表の Gold の材質・張力・音色・反応は[チェロ用の公式製品ページ](https://www.pirastro.com/public_pirastro/pages/en/Gold-00004/)に基づきます。発売年と推奨用途は、確認したチェロ用公式資料では未指定です。
- `docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md:15` — - 過去に挙げられた名称の販売時期・仕様は未確認
- `docs/strings/manufacturers/strings-manufacturer-savarez-corelli.md:29` — Corelli New Concept / Corelli Gut は、今回確認した公式資料では現行チェロ用シリーズとして確認できませんでした。過去に挙げられていた名称として区別し、現行比較表には含めません。過去の販売時期・仕様や終売時期も未確認であり、「掲載を確認できない」ことをもって終売とは断定しません。
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:15` — - 確認した一次資料では、全シリーズの発売年を確認できていない
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:26` —  /  Belcanto Gold  /  上級  /  steel 系列  /  深さと明瞭さの両立志向  /  しなやか寄り  /  室内楽、歌う表現  /  Belcanto との同一性は未確認  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:30` —  /  Superflexible  /  現行ライン  /  コア: A/D/G/C = rope core。巻線: A/D/G/C = chrome wound  /  未指定  /  未指定  /  未指定  /  型番 25/27/28/29、セット 31  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:31` —  /  Peter Infeld  /  現行ライン  /  コア: A/D = carbon steel、G/C = spiral rope。巻線: A/D = multialloy、G/C = tungsten/chrome  /  未指定  /  未指定  /  未指定  /  型番 PI41–PI44、セット PI400  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:32` —  /  Dominant Pro  /  現行ライン  /  コア: A/D = carbon steel、G/C = spiral core。巻線: A/D = chrome wound、G = nickel-alloy wound、C = tungsten/nickel-alloy  /  未指定  /  未指定  /  未指定  /  型番 DP41–DP44、セット DP400  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:33` —  /  Rondo Experience  /  現行ライン（A弦）  /  コア: A = carbon steel。巻線: A = multialloy wound。D/G/C = 未指定  /  未指定  /  未指定  /  未指定  /  チェロ用ページには A弦 RO41XP のみ掲載  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:34` —  /  Spirit!  /  現行ライン  /  コア: A/D = carbon steel、G/C = rope core。巻線: A/D/G/C = chrome wound  /  未指定  /  未指定  /  未指定  /  型番 SP41–SP44、セット SP400  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:35` —  /  Präzision  /  現行ライン  /  コア: A/D/G/C = carbon steel。巻線: A/D/G/C = chrome wound  /  未指定  /  未指定  /  未指定  /  型番 90/93/95/98、セット 102  / 
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:49` — 2026年10月23日に公式チェロ一覧で Belcanto Gold の掲載を確認しました。ただし、Belcanto から単に名称変更されたとする根拠は確認できていません。旧製品との同一性は型番・仕様で確認してください。
- `docs/strings/manufacturers/strings-manufacturer-thomastik-infeld.md:55` — この6シリーズのコアと巻線は、参考リンクに挙げた各チェロ用製品ページの「TECHNICAL DETAILS」に基づきます。いずれも掲載サイズは 4/4、ゲージは medium です。Rondo Experience は A弦 RO41XP のみ掲載されているため、D/G/C の仕様は未指定としています。音色・反応・推奨用途など、今回確認できなかった項目も未指定とし、発売年は補完していません。
- `docs/strings/manufacturers/strings-manufacturer-warchal.md:15` — - 発売年は Brilliant（2010年開発）以外、今回確認できた一次資料では未確認
