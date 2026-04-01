add_cus_dep('glo', 'gls', 0, 'makeglossaries');
add_cus_dep('acn', 'acr', 0, 'makeglossaries');
add_cus_dep('out', 'otl', 0, 'makeglossaries');

sub makeglossaries {
  my ($base, $ext) = @_;
  system( "makeglossaries \"$base\"" );
}