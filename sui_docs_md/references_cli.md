Sui provides a command line interface (CLI) tool to interact with the Sui network, its features, and the Move programming language. The complete suite of tools is called the Sui CLI, with commands grouped together by feature. Each group of commands is commonly referred to by its top-level command: Sui Client CLI, Sui Keytool CLI, Sui Move CLI, and Sui Validator CLI.

## Update CLI

The recommended way to manage Sui CLI installations and versions is via `suiup`: https://github.com/mystenLabs/suiup.

:::info

The `tracing` feature is important as it adds Move test coverage and debugger support in the Sui CLI. Unless it is enabled you will not be able to use these two features.

:::

## Sui CLI commands

There are a number of top-level commands available, but the six most useful to users are the following. Use the `help` flag for the commands that are not documented yet. For example, `sui validator --help`.

- **[Sui Client CLI](./cli/client.md):** Use the `sui client` commands to interact with the Sui network.
- **[Sui Client PTB CLI](./cli/ptb.md):** Use the `sui client ptb` command to build and execute PTBs.
- **[Sui Keytool CLI](./cli/keytool.md):** Use the `sui keytool` commands to access cryptography utilities.
- **[Sui Move CLI](./cli/move.md):** Use the `sui move` commands to work with the Move programming language.
- **[Sui Replay CLI](./cli/replay.md):** Use the `sui replay` command to replay a transaction and generate transaction traces for the Move Debugger and trace analysis tools.
- **[Sui Validator CLI](./cli/validator.md):** Use the `sui validator` commands to access tools useful for Sui validators.