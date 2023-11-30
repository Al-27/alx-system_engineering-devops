#!/usr/bin/env ruby
txt = ARGV[0]
from = txt.scan(/(?<=from:).*?(?=])/).join
to = txt.scan(/(?<=to:).*?(?=])/).join
flags = txt.scan(/(?<=flags:).*?(?=])/).join
puts "#{from},#{to},#{flags}"
