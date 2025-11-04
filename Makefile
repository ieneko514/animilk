SRCS := \
  entry.c

OBJS := $(patsubst %.c,%.o,$(SRCS))
DEPS := $(patsubst %.o,%.d,$(OBJS))

CC := clang --target=wasm32-unknown-unknown

WASM_MODULE := animilk_native.wasm

$(WASM_MODULE): $(OBJS)
	$(CC) -nostdlib -Wl,--export-dynamic -Wl,--no-entry $(LDFLAGS) $^ -o $@

-include $(DEPS)

%.o: %.c
	$(CC) -MD -MT $@ -MP -MF $(patsubst %.o,%.d,$@) -nostdinc $(CPPFLAGS) -fvisibility=hidden -c $(CFLAGS) $< -o $@

clean:
	rm -f $(DEPS) $(OBJS) $(WASM_MODULE)

.PHONY: clean
