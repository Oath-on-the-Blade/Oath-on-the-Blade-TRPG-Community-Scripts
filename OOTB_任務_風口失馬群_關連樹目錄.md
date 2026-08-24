# 《風口失馬群》關連樹目錄

> 關係索引文檔；不是資料夾、不是固定戰役。

- **根任務**：《風口失馬群》
- **根 `script_id`**：`ootb-script-fengkou-shimaqun`

## 節點與直接關連

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《風口失馬群》 | `ootb-script-fengkou-shimaqun` | — | 根任務 | 無 |
| 《北槽借印》 | `ootb-script-beicao-jieyin` | 《風口失馬群》 | 後續／北槽商路承接 | 非必要；可獨立運行 |
| 《北槽路上多了一道夜柵》 | `ootb-task-beicao-night-gate-001` | 《北槽借印》 | 後續／北槽路制度後果 | 非必要；可獨立運行 |
| 《北槽轉運場第十三秤總是輕三斤》 | `ootb-task-beicao-transfer-thirteenth-scale-001` | 《北槽路上多了一道夜柵》 | 後續／轉運與重量查核制度後果 | 非必要；可獨立運行 |
| 《北槽轉運場十五枚車轄有四枚先裂了》 | `ootb-task-beicao-transfer-linchpin-cracks-001` | 《北槽轉運場第十三秤總是輕三斤》 | 後續／輕車轉運器材安全後果 | 非必要；可獨立運行 |
| 《北槽轉運場九匹代騾有兩匹掛錯了鈴》 | `ootb-task-beicao-transfer-nine-mules-wrong-bells-001` | 《北槽轉運場十五枚車轄有四枚先裂了》 | 後續／替代運力與交接制度後果 | 非必要；可獨立運行 |

## 關連圖

```text
風口失馬群
└─→ 北槽借印
    └─→ 北槽路上多了一道夜柵
        └─→ 北槽轉運場第十三秤總是輕三斤
            └─→ 北槽轉運場十五枚車轄有四枚先裂了
                └─→ 北槽轉運場九匹代騾有兩匹掛錯了鈴
```

## 共同背景基線

- 白草風口、北槽水眼與商路變化可以形成持續地方背景；後作不得把前作某個嫌疑、人物去向或責任 branch 無聲改成全樹正史。
- 《北槽借印》明確承接《風口失馬群》的後續局勢，但不要求玩家完成前作；沒有前作存檔時仍有完整開場。
- 《北槽路上多了一道夜柵》承接《北槽借印》後至少一段時間的路務／秩序後果，只讀已保存的長期 state。
- 《北槽轉運場第十三秤總是輕三斤》承接《北槽路上多了一道夜柵》之後形成的重車轉運／重量查核習慣；前作 ending 只改變信任、文書便利與普通現場資源，不改本篇秤器作弊真相。
- 《北槽轉運場十五枚車轄有四枚先裂了》直接承接轉運場輕車使用與前篇持久 state；前篇 state 只改變查核便利、車流量與普通備用車資源，不改本篇車轄器材事故真相。
- 《北槽轉運場九匹代騾有兩匹掛錯了鈴》直接承接車轄事件後可能出現的替代運力與交接習慣；前篇 state 只改變查閱便利、代運壓力與備用馱騾數，不改本篇代騾識別錯配的客觀真相。
- `beicao_transfer_yard_short_closure = true`、`beicao_light_cart_service_slowdown = true`、`beicao_pack_mule_service_slowdown = true` 都是短期 state；只有當前存檔仍顯示相應普通檢修／重核未完成時，後作才可把它們當作有效 overlay，不得永久化。

## Branch／state 路由

### 通用規則
- 前作 ending 可改變北槽對玩家的信任、商路是否被視為安全及程序態度；不應直接替後作決定新的案情真相。
- 短期氣血、臨時場景資源及未保存的推論不沿樹自動傳遞。
- 沒有前作紀錄時，各 `independent` 後作使用自身預設狀態。
- 同一 ending 開啟後續不表示同源後續自動互斥；是否可並行／先後遊玩只看實際持久 state 是否衝突。

### 《北槽路上多了一道夜柵》→《北槽轉運場第十三秤總是輕三斤》
- `nightgate-safe-limited-passage`：商旅已接受「驗清後有限放行」的制度經驗；新篇第一次要求暫停重車 20 分鐘時不需說服。
- `nightgate-heavy-road-closed`：保留較完整臨時封重車格式；新篇取得兩項重量矛盾後可由當值文吏直接出具一個時段暫停放行單。
- `nightgate-safe-cause-unclear`：商旅對新一輪安全查核較不耐；新篇第一次要求全場停秤需先提出具體矛盾或完成正文說服。
- `nightgate-collapse`：轉運場會預置普通車楔／長木等救車資源；若存檔另保存同一批角色曾被可靠歸因為明知風險仍強令放車，官面只給必要查核權，不額外給無監看保管權。
- `nightgate-abandon`：使用新篇無前作基線；若存檔另保存道路損壞，只改可放行寬度，不改新篇真相。

### 《北槽轉運場第十三秤總是輕三斤》→《北槽轉運場十五枚車轄有四枚先裂了》
- `beicao_transfer_scale_sealed_check = true`：若事故車封存／貨袋記錄與出場時一致，新篇可直接排除「離場後臨時加重」作主要原因；不直接證明器材缺陷。
- `beicao_transfer_fraud_unresolved = true`：商旅對內部查核較敏感；全面暫停修車棚出庫前需先提出一項具體共同風險證據，或完成新篇正文說服。
- `beicao_transfer_fraud_unresolved = false`：白草驛保留較完整原始查核鏈；新篇可直接在場查閱近五日修車發料簿原件。
- `beicao_transfer_yard_short_closure = true` 且該短期 state 當前仍有效：輕車需求提高；新篇四枚問題車轄中已有 3 枚裝車，其中事故車之外仍有 2 輛在路上，轉運場只有 2 輛普通備用輕車。若該短期 state 已失效，新篇改用自身無前作基線：事故車之外只有 1 輛高風險車在路上，並有 4 輛普通備用輕車。
- 以上 overlay 可同時成立；只有 `beicao_transfer_fraud_unresolved = true/false` 彼此互斥。它們不改新篇器材責任的客觀答案。

### 《北槽轉運場十五枚車轄有四枚先裂了》→《北槽轉運場九匹代騾有兩匹掛錯了鈴》
- `beicao_cart_linchpin_batch_recalled = true`：驛務已習慣把器材識別與貨物／牲口所有權分開；新篇只要出現一項可核對鈴牌矛盾，當值吏可直接暫停新增派騾 20 分鐘。此 state 不證明換鈴責任。
- `beicao_cart_repair_liability_unresolved = true`：北口工人對再次查內部交接較敏感；新篇要看夜間換欄簿原件需先提出一項具體身份矛盾，或完成正文說服。
- `beicao_cart_repair_liability_unresolved = false`：白草驛保留較完整原始查核鏈；新篇可直接在場查閱租契、換欄簿與鈴牌領用簿原件。
- `beicao_light_cart_service_slowdown = true` 且該短期 state 當前仍有效：新篇九匹代騾之外只有 1 匹普通備用馱騾可即時調度；若該短期 state 已失效，使用新篇無前作基線的 3 匹備騾。
- 以上 overlay 可同時成立；只有 `beicao_cart_repair_liability_unresolved = true/false` 彼此互斥。它們不改新篇換鈴與無授權代騾的客觀答案。

## 《北槽轉運場第十三秤總是輕三斤》新增持久 state

以下 state 只由該篇正文相應 ending 建立，不由本目錄自行創造結局：

- `beicao_transfer_scale_sealed_check = true`：第十三秤及其他秤採用可核對的支點封存檢查；屬可累積制度 state。
- `beicao_transfer_fraud_unresolved = true/false`：表示該篇轉運秤作弊責任是否仍未證實；不同值互斥，以最新合法結局寫回為準。
- `beicao_transfer_yard_short_closure = true`：轉運場短期只處理輕車／騾運至完成普通檢修；不是永久關閉，也不自動封死本樹後續。

## 《北槽轉運場十五枚車轄有四枚先裂了》新增持久 state

以下 state 只由該篇正文相應 ending 建立：

- `beicao_cart_linchpin_batch_recalled = true`：該篇已知風險車轄與相應車輛完成安全召回／封存；屬可累積安全處置 state。
- `beicao_cart_repair_liability_unresolved = true/false`：該篇器材誤發／發現後隱瞞責任是否仍未證實；兩值互斥，以最新合法結局寫回為準。
- `beicao_light_cart_service_slowdown = true`：轉運場短期降低輕車出庫速度，直至普通安全覆核與替換件補齊；不是永久關閉，不自動封死本樹其他節點。

## 《北槽轉運場九匹代騾有兩匹掛錯了鈴》新增持久 state

以下 state 只由該篇正文相應 ending 建立：

- `beicao_pack_mule_identity_chain_restored = true`：九匹原租騾與本次額外代騾已採外觀／蹄鐵／鈴牌／收條交叉核對；屬可累積交接制度 state。
- `beicao_pack_mule_hire_liability_unresolved = true/false`：本篇無授權代騾與換鈴責任是否仍未證實；兩值互斥，以最新合法結局寫回為準。
- `beicao_pack_mule_service_slowdown = true`：因本篇延誤而短期重核九匹並補派急貨；普通重核完成後失效，不代表永久降低北槽運力。
- 本篇目前沒有預寫下一個關連節點；任何 ending 都不因出自本篇而自動關閉既有樹內節點。日後若新篇直接讀取上述 state，應把《北槽轉運場九匹代騾有兩匹掛錯了鈴》列為直接來源。

## 維護

本樹穩定根是《風口失馬群》；不可因後續《北槽借印》或其他節點較突出而另立第二份樹目錄文檔。新增後續應依實際讀取的專用 state 掛到最近直接來源；若只共享白草驛／北槽地區，則不構成直接關連。

新增後續若直接讀取《北槽轉運場九匹代騾有兩匹掛錯了鈴》的代騾識別、責任或短期代運 state，應把該篇列作直接來源；不得越過它只掛更早祖先作方便 anchor。
