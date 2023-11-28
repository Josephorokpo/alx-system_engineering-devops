#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide a string as a command-line argument."
else
  # Extract the argument
  input_string = ARGV[0]

  # Define the regular expression using the Oniguruma syntax
  regex = /School/

  # Check if the input string matches the regular expression
  if input_string =~ regex
    puts "The input string '#{input_string}' matches the pattern 'School'."
  else
    puts "The input string '#{input_string}' does not match the pattern 'School'."
  end
end
