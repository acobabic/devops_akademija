FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
WORKDIR /App

# Copy everything
COPY . ./
# Restore as distinct layers
RUN dotnet restore
# Build and publish a release
RUN dotnet publish -c example_dotnet_app -o out
# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0
# Create a volume at container startup and mount it to /App directory
VOLUME [ "/App" ]
WORKDIR /App
COPY --from=build-env /App/out .
ENTRYPOINT ["dotnet", "example_dotnet_app.dll"]
