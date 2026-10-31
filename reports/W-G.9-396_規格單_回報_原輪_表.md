# W-G.9-396 回報之附表：前置與驗之 100 呼叫（rc／stderr B／末列（耗時 s））

| # | 命令 | 前置（工項一之端 da2af6d） | 驗（工項二 20fa615） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（108） | `0`／`0`／`⇒ 紅 []；rc 0`（116） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（325） | `0`／`0`／`⇒ 紅 []；rc 0`（334） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（27） | `0`／`0`／`⇒ 紅 []；rc 0`（28） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（28） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（30） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（12） | `0`／`0`／`⇒ 紅 []；rc 0`（12） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（209） | `0`／`0`／`⇒ 紅 []；rc 0`（222） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（56） | `0`／`0`／`⇒ 紅 []；rc 0`（59） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（363） | `0`／`0`／`⇒ 紅 []；rc 0`（394） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（512） | `0`／`0`／`⇒ 紅 []；rc 0`（551） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（7） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（7） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（54） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（58） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（304） | `0`／`0`／`⇒ 紅 []；rc 0`（324） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1388） | `0`／`0`／`⇒ 紅 []；rc 0`（1352） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（27） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（19） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（20） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（19） | `0`／`0`／`⇒ 紅 []；rc 0`（19） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（223） | `0`／`0`／`⇒ 紅 []；rc 0`（232） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（267） | `0`／`0`／`⇒ 紅 []；rc 0`（277） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（37） | `0`／`0`／`⇒ 紅 []；rc 0`（37） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（27） | `0`／`0`／`⇒ 紅 []；rc 0`（28） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（18） | `0`／`0`／`⇒ 紅 []；rc 0`（19） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['H1 同一合併群之候選分屬三個末端塊 ⇒ 形「多」之競合·三端皆未達', 'M7', 'M13']；rc 1`（12） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `1`／`0`／`⇒ 紅 ['W4', 'N3']；rc 1`（9） | `0`／`0`／`⇒ 紅 []；rc 0`（11） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（147） | `0`／`0`／`⇒ 紅 []；rc 0`（155） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（42） | `0`／`0`／`⇒ 紅 []；rc 0`（43） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（694） | `0`／`0`／`⇒ 紅 []；rc 0`（716） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（119） | `0`／`0`／`⇒ 紅 []；rc 0`（128） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（86） | `0`／`0`／`⇒ 紅 []；rc 0`（98） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（261） | `0`／`0`／`⇒ 紅 []；rc 0`（282） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（8） | `0`／`0`／`紅項 [] 器紅 0`（9） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（269） | `0`／`0`／`⇒ 紅 []；rc 0`（273） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/pre/k6s3_pre_35.json` | `0`／`0`／`{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6…`（154） | `0`／`0`／`{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6…`（160） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/pre/k6s3_pre_00.json` | `0`／`0`／`{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6…`（113） | `0`／`0`／`{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6…`（117） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/pre/f8_pre_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（154） | `0`／`0`／`⇒ 紅 []；rc 0`（162） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/pre/f8_pre_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（113） | `0`／`0`／`⇒ 紅 []；rc 0`（120） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/pre/parity35_pre.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（329） | `0`／`0`／`⇒ rc 0（不符 0 項）`（350） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/pre/parity00_pre.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（240） | `0`／`0`／`⇒ rc 0（不符 0 項）`（244） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（264） | `0`／`0`／`⇒ 紅 []；rc 0`（281） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（964） | `0`／`0`／`⇒ 紅 []；rc 0`（997） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（936） | `0`／`0`／`⇒ 紅 []；rc 0`（968） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（113） | `0`／`0`／`⇒ 紅 []；rc 0`（121） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（351） | `0`／`0`／`⇒ 紅 []；rc 0`（374） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（263） | `0`／`0`／`⇒ 紅 []；rc 0`（277） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／`⇒ 紅 []；rc 0`（41） | `0`／`0`／`⇒ 紅 []；rc 0`（46） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（531） | `0`／`0`／`⇒ 紅 []；rc 0`（582） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（263） | `0`／`0`／`⇒ 紅 []；rc 0`（278） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（266） | `0`／`0`／`⇒ 紅 []；rc 0`（275） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（260） | `0`／`0`／`⇒ 紅 []；rc 0`（274） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（264） | `0`／`0`／`⇒ 紅 []；rc 0`（276） |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | `1`／`0`／`⇒ 紅 ['W2', 'W3']；rc 1`（7） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（268） | `0`／`0`／`⇒ 紅 []；rc 0`（277） |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（1） | `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（1） |
| `92` | `python3 verify/probes/probe_WG9398_rw25.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `93` | `python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `94` | `python3 tests/test_pool_slot.py` | `0`／`0`／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`（0） | `0`／`0`／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`（0） |
| `95` | `python3 verify/probes/probe_WG9399_k960x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `96` | `python3 verify/probes/probe_WG9399_k960x.py wiring <repo> bd7da4d` | `0`／`0`／`⇒ 紅 []；rc 0`（14） | `0`／`0`／`⇒ 紅 []；rc 0`（15） |
| `97` | `python3 verify/probes/probe_WG9399_k960x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（265） | `0`／`0`／`⇒ 紅 []；rc 0`（275） |
| `98` | `python3 verify/probes/probe_WG9396_k960m.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['H1', 'H1′', 'H2', 'H3', 'H4', 'H5', 'H7', 'H8', 'H6']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `99` | `python3 verify/probes/probe_WG9396_k960m.py wiring <repo> 9fd3427` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3']；rc 1`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `100` | `python3 verify/probes/probe_WG9396_k960m.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（267） | `0`／`0`／`⇒ 紅 []；rc 0`（277） |
