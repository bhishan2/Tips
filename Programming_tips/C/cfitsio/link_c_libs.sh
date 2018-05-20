# ls /opt/local/lib/*fit*

# We get:
# /opt/local/lib/libcfitsio.5.3.39.dylib
# /opt/local/lib/libcfitsio.5.dylib
# /opt/local/lib/libcfitsio.a
# /opt/local/lib/libcfitsio.dylib

# ln -s /opt/local/lib/libcfitsio.5.3.39.dylib  /usr/local/lib/libcfitsio.5.3.39.dylib
# ln -s /opt/local/lib/libcfitsio.5.dylib /usr/local/lib/libcfitsio.5.dylib
# ln -s /opt/local/lib/libcfitsio.a /usr/local/lib/libcfitsio.a
# ln -s /opt/local/lib/libcfitsio.dylib /usr/local/lib/libcfitsio.dylib


# Now include fitsio.h  header file:
# ls /opt/local/include/*fit*

# We get:
# /opt/local/include/fitsio.h
# /opt/local/include/fitsio2.h

# ln -s /opt/local/include/fitsio.h /usr/local/include/fitsio.h
# ln -s /opt/local/include/fitsio2.h /usr/local/include/fitsio2.h

# We also need longnam.h
# ls /opt/local/include/*long* # /opt/local/include/longnam.h

# ln -s /opt/local/include/longnam.h /usr/local/include/longnam.h