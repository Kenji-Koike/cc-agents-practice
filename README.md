# Claude Code `/agents` コマンド ハンズオン

Claude Code の `/agents` コマンドを使ってカスタムエージェントを作成・活用するハンズオンです。
基礎から応用まで段階的に学べます。

## 前提知識

- Claude Code の基本操作（ファイル編集、コマンド実行）
- Git の基本操作

## カリキュラム構成

| レベル | タイトル | 概要 |
|--------|----------|------|
| [Level 1](./exercises/level1/) | エージェントの基礎理解 | `/agents` の概念と仕組みを理解する |
| [Level 2](./exercises/level2/) | 初めてのカスタムエージェント | シンプルなエージェントを作成する |
| [Level 3](./exercises/level3/) | ツール制限とスコープ | 特定のツールだけを持つ専門エージェント |
| [Level 4](./exercises/level4/) | 実践：コードレビューエージェント | 実用的なエージェントを構築する |
| [Level 5](./exercises/level5/) | マルチエージェント連携 | 複数エージェントを組み合わせたワークフロー |

## エージェントとは

Claude Code のエージェントは `.claude/agents/` ディレクトリに配置するMarkdownファイルで定義します。
各エージェントは専用の **システムプロンプト** と **利用可能なツール** を持ちます。

```
.claude/
└── agents/
    ├── my-reviewer.md    ← カスタムエージェント定義
    └── my-analyzer.md
```

エージェントを呼び出すと、Claude Code はそのエージェントの設定に従った
サブエージェントとして動作します。メインの会話コンテキストを汚染せずに
独立したタスクを実行できます。

## はじめ方

```bash
# リポジトリをクローン後、cc-agents-practice ディレクトリで Claude Code を起動
cd cc-agents-practice
claude
```

Level 1 から順番に進めてください。
