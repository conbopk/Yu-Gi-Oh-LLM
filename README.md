# LLM From Scratch

Small decoder-only Transformer implemented in PyTorch, trained from scratch to generate Yu-Gi-Oh cards. The decoder architecture is based on [Attention Is All You Need](https://arxiv.org/pdf/1706.03762)

## Prerequisites

- **Python 3.12**
- **[uv](https://docs.astral.sh/uv/)** - the project uses `uv` for dependency and environment management. Install it first:
    ```bash
    # macOS / Linux 
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Windows
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

## Folders

- `src/llm_from_scratch/`: model, tokenizer, dataset, and checkpoint code.
- `scripts/`: runnable scripts for data prep, training, and inference.
- `data/`: raw and processed datasets.
- `model/`: saved training runs and checkpoints.
- `test/`: unit tests for tokenizer, checkpoint and transformer architecture.


## Setup

```bash
uv sync
```

Optional W&B logging:

```bash
uv run wandb login
```

Create `.env` file and copy content from `.env.example` and complete file

```bash
WANDB_API_KEY="your-w&b-project-key"
```

Set `use_wandb=True`, `wandb_entity`, and `wandb_project` in `scripts/train.py` to enable logging. Training and model settings live in `TRAIN_CONFIG` and `MODEL_CONFIG`.

## Scripts

Run in order:

```bash
uv run scripts/download_data.py
uv run scripts/create_dataset.py
uv run scripts/build_tokenizer.py
uv run scripts/train.py
uv run scripts/inference.py
uv run scripts/open_pack.py
```

- `download_data.py`: downloads the raw Yu-Gi-Oh card dataset.
- `create_dataset.py`: converts raw card rows into train/validation text files.
- `build_tokenizer.py`: builds the char and BPE tokenizers.
- `train.py`: trains the Transformer and writes checkpoints to `model/`.
- `inference.py`: loads a checkpoint and generates card text.
- `open_pack.py`: opens a booster pack of generated cards from your cli :).

Use `checkpoint.pt` to resume training and `best_model.pt` for inference.


### Sample card pack

```text
Press Enter to open pack...
Opening pack...

Press Enter to reveal card 1/5...

+--------------------------------------------------------------------------------+                                                                   
| CARD 1/5                                                            ULTRA RARE |                                                                   
|                      Number C32: Shark Gainpplebis Spider                      |                                                                   
+--------------------------------------------------------------------------------+                                                                   
| type: monster                                                                  |                                                                   
| sub_type: [sea serpent／xyz／effect]                                             |
| attribute: water                                                               |
| rank: rank 4                                                                   |
| attack: 2500                                                                   |
| defense: 2400                                                                  |
| description: 3 level 4 monstersyou can also xyz summon this card by using a    |
| "number 69: heraldry crest". (transfer its materials to this card.) gains def  |
| equal to the original atk of the opponent's monster that has no xyz materials: |
| you can detach all materials from this card, then activate 1 of these          |
| effects.●each turn, this card gains 500 atk.●when it is targeted for an        |
| attack: you can detach 1 xyz material from this card; negate the attack, then  |
| you can make up to 3 attacks on monsters during each battle phase, also you    |
| sent to the graveyard, also for the rest of this turn, your opponent takes no  |
| damage from your hand.                                                         |
+--------------------------------------------------------------------------------+

Press Enter to reveal card 2/5...

+--------------------------------------------------------------------------------+                                                                   
| CARD 2/5                                                            ULTRA RARE |                                                                   
|                         Neo Blue-Eyes Ultimate Dragon                          |                                                                   
+--------------------------------------------------------------------------------+                                                                   
| type: monster                                                                  |                                                                   
| sub_type: [dragon／effect]                                                      |
| attribute: light                                                               |
| rank: level 7                                                                  |
| attack: 2400                                                                   |
| defense: 1500                                                                  |
| description: cannot be normal summoned/set. must first be special summoned     |
| (from your hand) by banishing 1 fire monster from your gy. you can only        |
| special summon "neonoble arms cannot special summon "noble arms                |
| specialalaceel" once per turn this way. if this card declares an attack, it    |
| can make a second attack during each battle phase.                             |
+--------------------------------------------------------------------------------+

Press Enter to reveal card 3/5...

+--------------------------------------------------------------------------------+                                                                   
| CARD 3/5                                                                COMMON |                                                                   
|                              Aleister The Invoker                              |                                                                   
+--------------------------------------------------------------------------------+                                                                   
| type: monster                                                                  |                                                                   
| sub_type: [spellcaster／effect]                                                 |
| attribute: dark                                                                |
| rank: level 4                                                                  |
| attack: 1200                                                                   |
| defense: 1400                                                                  |
| description: you can send this card from your hand to the gy; special summon 1 |
| "gravekeeper's" monster or 1 ritual spell from your hand, except               |
| "gravekeeper's nobleman". during your opponent's turn (quick effect): you can  |
| target 1 "noble knight" monster you control; equip this card to that target.   |
| you can only use each effect of "noble arms - almace"" once per turn.          |
+--------------------------------------------------------------------------------+

Press Enter to reveal card 4/5...

+--------------------------------------------------------------------------------+                                                                   
| CARD 4/5                                                            ULTRA RARE |                                                                   
|                              Roar, The Infer King                              |                                                                   
+--------------------------------------------------------------------------------+                                                                   
| type: monster                                                                  |                                                                   
| sub_type: [spellcaster／effect]                                                 |
| attribute: fire                                                                |
| rank: level 8                                                                  |
| attack: 2800                                                                   |
| defense: 2800                                                                  |
| description: cannot be normal summoned/set. must be special summoned by its    |
| own effect. during your opponent's main phase (quick effect): you can target 1 |
| "nekroz" monster you control; this turn, it can make a second attack during    |
| each battle phase this turn. if this card attacks, it is changed to defense    |
| position at the end of the battle phase, and if it was a "nekroz" monster, you |
| can return this card from the field to the hand. you can only use this effect  |
| of "nekroz of catastor" once per turn.                                         |
+--------------------------------------------------------------------------------+

Press Enter to reveal card 5/5...

+--------------------------------------------------------------------------------+                                                                   
| CARD 5/5                                                 PRISMATIC SECRET RARE |                                                                   
|                            Gaia Soul The Fire Kings                            |                                                                   
+--------------------------------------------------------------------------------+                                                                   
| type: spell                                                                    |                                                                   
| sub_type: quick-play                                                           |
| description: target 1 face-up monster your opponent controls (quick effect):   |
| destroy it. you can only activate 1 "fire formation - tenki" per turn.         |
+--------------------------------------------------------------------------------+

Pack Summary
------------
1. Ultra Rare         number c32: shark gainpplebis spider
2. Ultra Rare         neo blue-eyes ultimate dragon
3. Common             aleister the invoker
4. Ultra Rare         roar, the infer king
5. Prismatic Secret Rare gaia soul the fire kings
```