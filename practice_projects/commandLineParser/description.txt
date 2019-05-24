The purpose of this command line parser is to take line of input and parse it
into its constituent parts: command, flags, and (one) required argument.

Specs:

  Command:
  - First part of the input.
  - Consists of alphabetic characters.
  - Can be of any length.
  - Only one command per input.

  Flags:
  - Second part of the input.
  - Consists of a hyphen (-) followed by one alphabetic character.
  - Can have [0,infinity) flags per input.

  Argument:
  - Final part of the input.
  - Consists of alphanumeric characters.
  - Can be of any length.
  - Only one argument per input.
