# 戰役總劇本：紙關暗印

- `campaign_id`: `ootb-campaign-paper-pass-hidden-seal`
- 總劇本版本：1.0.0
- 戰役狀態：連載中
- 已完成未發布階段：01、02、03（僅存在 `campaign_in_progress`；尚未合併 default）
- 當前規劃階段：04；01–03 已完成作者稿
- 共同起點與地理：承泰二十一年，昊國一座道內河運與驛路交會的普通州城及其近郊紙坊、驛站、河關；不指定既有正典城市、官署具名人物或門派
- 等級／規模走向：4–6級小型 → 6–8級中型 → 8–11級中型 → 10–13級大型
- 共用世界權威：`世界知識庫/README.md`、`世界知識庫/地理與世界基準/時代與世界基準.md`；劇本不新增全世界正典人物或組織
- repository 總綱只保存作者權威；單桌實際 NPC 姓名、例外狀態、已裁定承接與 `campaign_save` 不寫回本檔

## 跨篇核心答案
州城一名承印作坊帳房與河關外的票據掮客合作，利用官紙裁邊餘料、作廢驗印樣與合法貨票的時間差，製作只能短時間騙過遠看與夜間查驗的假通行票。最初目的只是讓少量私貨避開重複查驗；掮客後來把這套方法賣給更多貨主，導致假票數量增加。河關一名夜班書吏收錢替部分票據補記日期，但不知道作坊帳房已把同一套紙料來源擴大出售。

核心危機不是朝廷制度整體腐敗，也沒有超自然力量。真正問題是三個彼此利益不同的地方行動者把合法流程的不同縫隙串成可重複利用的短窗口：帳房提供紙料與仿印技法，掮客配對貨主與時段，書吏提供少量真實格式與夜班補記。三人互相需要，又都只掌握部分鏈條。

戰役開始前，裁邊餘料外流、少量假票成功通關、書吏補記與掮客收費都已發生。尚未發生的是一次大批量集中使用：掮客正準備在十日內替一批高價私貨同時安排河關與驛路兩條出口。玩家若介入，這個計畫會依證據、人物自由狀態與查驗警戒改變，不保證按原時序發生。

## 跨篇真實時間線
1. 三月前：承印作坊帳房發現裁邊餘料與作廢驗印樣的銷毀登記可被做出小額差異。
2. 兩月前：票據掮客買下第一批餘料，試作少量假通行票；因只在夜間遠查使用而成功。
3. 一月前：河關夜班書吏為還私人債務，開始收錢補記少量日期與班次，誤以為只是替熟商補手續。
4. 十日前：掮客確認可把紙料、補記與貨主時段串起來，接下大批量私貨生意。
5. 戰役開始：紙坊清點時發現「四束裁邊紙中有一束重量總少半斤」，形成01。
6. 若01留下紙料來源或交易接口，帳房／掮客會因查核風險改變交付地點，形成02。
7. 若02使補記班次或掮客時段暴露，河關夜班窗口被迫提前使用或關閉，形成03。
8. 只有03仍留下可承接的大批量出貨接口時，兩路假票集中使用才形成04；若接口永久失去，戰役於相應 ending 提早收束。

## 跨篇主要行動者
### `actor_accountant`／`NPC#1@戰役:紙關暗印`
承印作坊帳房；姓名欄 `姓?-名?`；首次規劃／正式登場：01。知道餘料、作廢樣、自己交給掮客的批次與收款；不知道每名最終貨主。利益是持續抽成並避免作坊追責。資源是清點簿、銷毀登記、紙料接觸權與兩名臨時搬運工；限制是無權改正式官印與河關紀錄。若 `paper_source=proven` 或 `inspection_alert=raised|lockdown`，會停止原取料法、嘗試銷毀私人收款簿並把剩餘餘料交給掮客一次性帶走。若被拘留、死亡或確定倒戈，不再產生新指令。

### `actor_broker`／`NPC#2@戰役:紙關暗印`
票據掮客；姓名欄 `姓?-名?`；首次規劃：01，正式登場：02。知道假票使用者、交付時段、書吏可補記的班次與大批量私貨計畫；不知道承印作坊完整內帳。利益是完成大單、保住買賣網並避免替貨主頂罪。資源是短工、臨時藏貨點、貨主聯絡與假票成品；限制是沒有合法查驗權。若 `broker_route=exposed`，會分拆貨物；若書吏退出，會改走只有假票、風險更高的驛路方案。

### `actor_clerk`／`NPC#3@戰役:紙關暗印`
河關夜班書吏；姓名欄 `姓?-名?`；首次規劃：01，正式登場：03。知道自己補過哪些日期與班次，知道掮客外貌／聯絡法，不知道紙料來源與全部貨主。利益是還債、保住差事、避免因大案被當主謀。資源是夜班格式知識與少量補記機會；限制是不能單獨改白日總簿。若得知大批量私貨會把自己暴露，且玩家提供可信合法出路，會合作；若受威脅則可能逃走。

### `actor_carriers`
使用假票的數名地方貨主與短工集合 actor，沒有單一 NPC 實體。利益是降低查驗成本與避免私貨被扣；彼此沒有共同政治目的。當 `inspection_alert` 升高時，部分貨主退出，剩餘者要求掮客集中一次出貨。

### `actor_inspection`
地方紙坊清點與河關查驗制度 actor，沒有單一 NPC 實體。初始只見零散帳物差異。能在有可核對證據時封存紙料、比對班次、暫停夜班補記並加派查驗；不能憑玩家猜測無限搜查。

## 戰役級 NPC registry
- `NPC#1@戰役:紙關暗印`：`姓?-名?`；`actor_accountant`；承印作坊帳房；首次規劃／正式登場01。
- `NPC#2@戰役:紙關暗印`：`姓?-名?`；`actor_broker`；票據掮客；首次規劃01、正式登場02。
- `NPC#3@戰役:紙關暗印`：`姓?-名?`；`actor_clerk`；河關夜班書吏；首次規劃01、正式登場03。
以上編號永久保留；死亡、退出、未登場或改版均不得重用。各篇本地人物若不跨篇，不升格為戰役級 NPC。

## Campaign state
- `paper_source`: unknown | suspected | proven | sealed
- `broker_route`: unknown | traced | exposed | broken
- `clerk_link`: unknown | suspected | confirmed | severed
- `batch_cargo`: planned | split | moving | seized | dispersed
- `actor_accountant_status`: free | watched | cooperating | detained | escaped | dead
- `actor_broker_status`: free | watched | detained | escaped | dead
- `actor_clerk_status`: active | cooperating | suspended | detained | escaped | dead
- `inspection_alert`: low | raised | lockdown
- `public_attribution`: none | local_forgery_ring | broad_office_blame
- `campaign_status`: active | partly_completed | failed | completed
- `campaign_progress`: 已結算階段數/4

## State 權威表
- `paper_source`（01建立；unknown/suspected/proven/sealed）：紙料外流證明程度；02、03、04讀取，決定可否合法擴大比對與是否仍有新餘料。
- `broker_route`（02建立；unknown/traced/exposed/broken）：掮客交接路線暴露程度；03、04讀取，改變貨物分拆與追查入口。
- `clerk_link`（02建立；unknown/suspected/confirmed/severed）：夜班補記鏈證明／存續狀態；03、04讀取。
- `batch_cargo`（02建立；planned/split/moving/seized/dispersed）：大批量貨物的實際物流狀態；03、04讀取。
- 三個 `actor_*_status`：各自首次由人物可被處置的階段建立；後篇只按已保存狀態決定本人能否行動，不復活、不重置。
- `inspection_alert`（01建立；low/raised/lockdown）：合法查驗警戒；02–04讀取，增加查驗資源並促使貨主退出／集中。
- `public_attribution`（04建立；none/local_forgery_ring/broad_office_blame）：公開歸因結果；只有證據鏈足夠才可寫入 local_forgery_ring；broad_office_blame 只可保存為錯誤／過度歸因的世界後果，不能當作已證實真相。
- `campaign_status`、`campaign_progress`：每篇結算寫入；前者記 active/partly_completed/failed/completed，後者記已正式結算階段數/4。

後續只保存會被實際讀取的值。人物例外狀態若超出枚舉，由單桌 `campaign_save` 保存；總綱不預寫所有例外。

## 01：四束裁邊紙有一束總少半斤
- 狀態：規劃
- 預定 `script_id`: `ootb-campaign-paper-pass-hidden-seal-01`
- 預定正式檔：`OOTB_戰役任務_紙關暗印(01)_四束裁邊紙有一束總少半斤.md`
- 建議：4–6級，R5，小型
- 輸入 state：共同起點；`paper_source=unknown, broker_route=unknown, inspection_alert=low`
- 直接使用：`NPC#1@戰役:紙關暗印`；`NPC#2` 只可透過已成立交易痕跡被提及，不要求本篇實體登場
- 為甚麼現在：紙坊月末清點首次把裁邊紙按重量與銷毀登記交叉核對，差額剛好跨過可視為潮濕／裁切誤差的範圍。
- 玩家介入理由：作坊東家／管事需要外部江湖人協助在不驚動全部工人的情況下查清短缺，並看守下一次銷毀搬運；角色可因受僱、既有地方名氣或恰在附近接短工介入。
- 獨立目標：找出本次裁邊紙短缺的責任、去向與可核對證據，阻止下一批餘料被帶走；本篇結束時紙坊本次短缺必須獨立結算。
- 局部真相：帳房利用稱重與銷毀登記的時間差，每次抽走少量裁邊餘料，交給不知名買家；搬運工只收錢把封好的紙束換位置，不知道用途。
- 與跨篇真相接觸：可取得收款記號、交付時段或紙纖維／裁邊規格，證明短缺並非單純偷紙自用；不要求本篇查出假票完整用途。
- 主要輸出：`paper_source`、`actor_accountant_status`、`inspection_alert`。
- `PA01_E01` 帳鏈坐實：`paper_source=proven, inspection_alert=raised`；帳房被控制或合作均可。可承接02；`active,1/4`。
- `PA01_E02` 去向有痕：`paper_source=suspected` 且取得有效交付時段／記號；帳房仍可自由。掮客因察覺風險改交付地。可承接02；`active,1/4`。
- `PA01_E03` 只止住本次短缺：餘料回收、責任落在搬運層，但交易接口永久失去。提早結局《紙束歸秤》：紙坊補做銷毀清點並追回本批損失；最後只留下幾張已被裁成陌生尺寸的紙角，無可靠方向可追。`partly_completed,1/4`；02–04不再發生為本戰役篇章。
- `PA01_E04` 放棄：本次清點由作坊自行處理，角色退出；`failed,1/4`。

## 02：兩處交紙棚有一處總在換班前先空一刻
- 狀態：規劃
- 預定 `script_id`: `ootb-campaign-paper-pass-hidden-seal-02`
- 預定正式檔：`OOTB_戰役任務_紙關暗印(02)_兩處交紙棚有一處總在換班前先空一刻.md`
- 建議：6–8級，R7，中型
- 解鎖路線：01已正式裁定可承接，且 `PA01_E01 OR PA01_E02`。E01由坐實紙料鏈＋查驗升高令掮客換點；E02由有效交付時段／記號令玩家可追到換點。若01為E03/E04，本篇鎖定。
- 輸入：`paper_source`、`actor_accountant_status`、`inspection_alert`
- 直接使用：`NPC#1`（視狀態）、`NPC#2`
- 為甚麼現在：掮客收到原交付點可能暴露的消息，把一次既定交紙改到兩處棚屋輪換，換班前的空檔成為唯一穩定交接窗口。
- 玩家介入理由：01已取得的交易痕跡／合作口供直接指向時段；不是新委託。
- 獨立目標：確認買紙者、截住本次交付、取得可核對的後續路線；本篇需獨立處理本次交接與涉事人員。
- 局部真相：掮客以兩棚輪換混淆跟蹤，短工只知道搬紙與收款；部分紙已被裁成票據尺寸，但尚未全部印成假票。
- 接觸跨篇真相：可揭露假票用途、掮客與夜班班次的聯絡記號之一。
- 主要輸出：`broker_route`、`clerk_link`、`batch_cargo`、`actor_broker_status`。
- `PA02_E01` 掮客鏈曝光：`broker_route=exposed, clerk_link=suspected, batch_cargo=split`；可承接03；`active,2/4`。
- `PA02_E02` 只追到班次：`broker_route=traced, clerk_link=suspected, batch_cargo=planned`；可承接03；`active,2/4`。
- `PA02_E03` 交接已止但所有夜班接口永久失去：提早結局《空棚封紙》；本次紙料與短工處理完畢，角色知道有人買紙做假票，卻沒有可核對的人或班次再追。最後一拍是某張半成票上留有被刮去的時刻欄。`partly_completed,2/4`；03–04鎖定。
- `PA02_E04` 放棄：`failed,2/4`。

## 03：三本夜班簿有一本總在落鎖後多一行
- 狀態：規劃
- 預定 `script_id`: `ootb-campaign-paper-pass-hidden-seal-03`
- 預定正式檔：`OOTB_戰役任務_紙關暗印(03)_三本夜班簿有一本總在落鎖後多一行.md`
- 建議：8–11級，R10，中型
- 解鎖路線：02已裁定可承接，且 `(PA02_E01 AND clerk_link=suspected) OR (PA02_E02 AND broker_route=traced)`；同時帶入01形成的 `paper_source`，用於決定查驗方是否可合法擴大比對。E03/E04鎖定。
- 輸入：此前全部有效 state，尤其 `paper_source/broker_route/clerk_link/inspection_alert`
- 直接使用：`NPC#2`（視狀態）、`NPC#3`
- 為甚麼現在：掮客察覺交紙線受查，要求書吏提前補完最後幾筆班次；書吏第一次發現數量遠超自己以為的「熟商補手續」。
- 玩家介入理由：02留下的班次／半成票／掮客口供可合法指向夜班比對。
- 獨立目標：查明補記責任、阻止本輪假票取得可信班次、決定書吏與掮客本次行為的處置；本篇須獨立結算河關夜班問題。
- 局部真相：書吏確實收錢補記，有責；他不知道紙料來源，也未策劃大批量私貨。掮客利用其有限補記，把不同貨主假票拼成看似分散的正常通行。
- 接觸跨篇真相：大批量私貨的兩路出口、預定時段與部分貨主退出／集中反應。
- 主要輸出：`clerk_link`、`actor_clerk_status`、`batch_cargo`、`inspection_alert`。
- `PA03_E01` 補記鏈坐實且取得大批量時段：`clerk_link=confirmed, batch_cargo=moving, inspection_alert=lockdown`；可承接04；`active,3/4`。
- `PA03_E02` 書吏合作、掮客改走驛路：`clerk_link=severed, actor_clerk_status=cooperating, batch_cargo=moving`；合作口供提供驛路時段；可承接04；`active,3/4`。
- `PA03_E03` 夜班問題已處理但集中出貨接口永久失去：提早結局《夜簿落鎖》；河關撤換補記權限、涉事書吏受處置，本次制度漏洞關閉。最後只留下幾張無法連回貨主的假票碎片。`partly_completed,3/4`；04鎖定。
- `PA03_E04` 放棄：`failed,3/4`。

## 04：兩路貨票有一路總在天亮前先過關
- 狀態：規劃
- 預定 `script_id`: `ootb-campaign-paper-pass-hidden-seal-04`
- 預定正式檔：`OOTB_戰役任務_紙關暗印(04)_兩路貨票有一路總在天亮前先過關.md`
- 建議：10–13級，R12，大型
- 解鎖路線：03已裁定可承接，且 `PA03_E01 OR PA03_E02`；同時讀取01的 `paper_source`、02的 `broker_route` 與03的 `clerk_link`。E01路線由河關封鎖迫使剩餘貨主集中改線；E02路線由書吏合作口供直接給出驛路時段。任何較早提早結局均使本篇鎖定。
- 輸入：全部仍有效 campaign state
- 直接使用：`NPC#1`、`NPC#2`、`NPC#3`，依各自狀態決定實體登場、口供、缺席或既有指令效果
- 為甚麼現在：剩餘貨主知道窗口即將永久關閉，要求掮客在天亮前完成最後一次集中出貨；若掮客已被控制，已付款短工仍會按既定指令搬運一次，但不產生新策劃。
- 玩家介入理由：03結算已正式固定可承接時段與出口；角色已有本戰役前史、證據與查驗方資格。
- 獨立目標：處理這次集中出貨，辨明假票鏈各人的實際責任，截斷仍在運作的紙料／票據／查驗接口，完成整條戰役結算。
- 局部真相：兩路貨物並非同一主人；部分只是逃避重複查驗，部分涉及高價私貨。掮客把不同貨主拼成同一窗口以提高收益。末篇不把所有貨主改寫成同一巨大陰謀。
- 核心接觸：玩家可直接接觸假票成品、剩餘紙料、班次鏈、掮客名單與實際集中出貨，足以處理戰役核心因果。
- 主要輸出：`batch_cargo`、三名 actor 狀態、`public_attribution`、`campaign_status`。
- `PA04_E01` 鏈條完整坐實且主要貨物截下：`batch_cargo=seized, public_attribution=local_forgery_ring, campaign_status=completed`；`completed,4/4`。
- `PA04_E02` 核心鏈斷但部分貨物散去：`batch_cargo=dispersed, public_attribution=local_forgery_ring, campaign_status=completed`；主要造假接口已不可再用，逃掉貨主保留為世界後果；`completed,4/4`。
- `PA04_E03` 只保住關口、未能坐實全部責任：本次集中出貨被阻，紙料／補記接口被封，但部分責任只能停在已證實範圍；`campaign_status=completed`，不得無證據擴大歸罪；`completed,4/4`。
- `PA04_E04` 放棄：剩餘出貨依當時 state 推進；`campaign_status=failed, campaign_progress=4/4`。

## 反應規則
- 若 `paper_source=proven|sealed`：帳房不能再穩定取得新餘料；後續只可使用已外流存量。
- 若 `actor_accountant_status=detained|dead|cooperating`：帳房不再下新指令；掮客只能按既有交易與存量反應。
- 若 `broker_route=exposed|broken`：掮客失去固定交接點，必須分拆貨物或使用成本更高、風險更大的臨時路線。
- 若 `actor_broker_status=detained|dead`：只有已付款短工可完成一次既定搬運；不能憑空產生新的掮客計畫。
- 若 `actor_clerk_status=cooperating|suspended|detained|dead`：夜班補記窗口關閉；已製成票據不會因此消失。
- 若 `inspection_alert=lockdown`：合法查驗資源增加，但貨主也會更快退出或集中一次出貨；不自動等於玩家知道所有藏貨點。
- 若任何關鍵 actor 出現總綱未列的意外狀態，GM 依 current `campaign_save` 保存；後篇只以可成立的代用品承接，例如既有帳冊、已付款指令或合作口供，不復活人物、不補造完美備份。

## 公開歸因邊界
只有取得足以連結紙料來源、掮客交易與夜班補記的證據，才可把事件公開歸因為 `local_forgery_ring`。缺其中一環時，只能處理已證實的個人／局部責任。不得因少數地方人員犯案推導整個官署、全道商旅或任何門派共同涉案。

## 末篇收束原則
04必須先完成本次集中出貨的成敗與人物處置，再結算戰役。玩家應能理解紙料如何外流、假票如何被製成、補記如何提供短窗口、掮客如何把多名貨主拼成一次大單。若證據不足，只公開到已證實範圍；未知部分保持未知，不以末篇旁白替玩家補答案。

## 版本與發布規則
總綱每次新增戰役級 NPC、state、主要 ending 或改變篇章接口，必須升版並重新通過 `戰役總劇本檢查.md`。未完成的階段只提交 `campaign_in_progress`。只有四階段全部完成、各自通過一般 Phase B，且總綱＋全部階段通過 `戰役整體覆檢.md` 後，才可向最新 default 安全 rebase／merge。