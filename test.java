public static Map<String, Object> flatten (Map<String, Object> map) { return map.entrySet().stream() .flatMap(FlatMapUtil::flotten) .collect (LinkedHashMap::new, (m, e) -> m.put("/" + e.getKey(), e.getValue()), LinkedHashMap::putALL);

private static Stream<Hap.Entry<String, Object>> flatten (Hap.Entry<String, Object> entry) {

if (entry == null) {

return Stream.empty();

}
if (entry.getValue() instanceof Map<?, ?>) {

return ((Map<?, ?>) entry.getValue()).entrySet().stream()
.flatMap(e -> flatten (new AbstractMap.SimpleEntry>(entry.getKey() + "/" + e.getKey(), e.getValue())));
if (entry.getValue() instanceof List<?>) {
List<?> list = (List<?>) entry.getValue(); return IntStream.range(0, list.size()) IntStream
.mapToObj(1->new AbstractMap.SimpleEntry<String, Object> (entry.getKey()+"/"+1, list.get(i))) Stream<AbstractMap< SimpleEntry>> .flatMap(FlatMapUtil::flatten);

}

return Stream.of(entry);