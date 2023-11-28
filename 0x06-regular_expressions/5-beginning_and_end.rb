#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide a string as a command-line argument."
else
  # Extract the argument
  input_string = ARGV[0]

  # Define the regular expression
  regex = /\Ah.n\z/

  # Check if the input string matches the regular expression
  if input_string =~ regex
    puts '$'
  else
    puts "#{input_string}$"
  end
end
